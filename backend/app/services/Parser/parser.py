import io
import json
import subprocess
import tempfile
from .types import Metadata, Content, Artical, Reference, Author
from typing import AnyStr, Dict, List, Optional
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import re


def _find_text_single(node: Element, xPath: AnyStr, namespaces: Dict) -> Optional[AnyStr]:
    """
    Helper functions for parsing XML for metadata

    :param node: The node to search from
    :param xPath: The xPath to search for
    :param namespaces: The namespaces to use
    :return: The text of the element found, or None
    :note: This function can only be used to parse the single text
    """

    element = node.find(xPath, namespaces=namespaces)
    return element.text if element is not None else None


def _find_text_paragraph(node: Element, xPath: AnyStr, namespaces: Dict) -> Optional[AnyStr]:
    """
    Helper functions for parsing XML for metadata

    :param node: The node to search from
    :param xPath: The xPath to search for
    :param namespaces: The namespaces to use
    :return: The text of the element found, or None
    :note: This function can only be used to parse the text paragraph
    """
    # Find all <div> elements specified by the XPath
    div_elements = node.findall(xPath, namespaces=namespaces)
    paragraphs_text = []

    for div in div_elements:
        # Check if this <div> contains a <head>. Skip it if yes.
        if div.find('.//tei:head', namespaces=namespaces) is None:
            # For each <div> without a <head>, concatenate the text of all <p> elements
            for p in div.findall('.//tei:p', namespaces=namespaces):
                text = " ".join(p.itertext())
                if text:
                    paragraphs_text.append(text.strip())

    # Return concatenated text of all paragraphs, separated by a space
    return " ".join(paragraphs_text) if paragraphs_text else None


def _find_words_list(node: Element, xPath: AnyStr, namespaces: Dict) -> Optional[List[AnyStr]]:
    """
    Helper functions for parsing XML for list of words

    :param node: The node to search from
    :param xPath: The xPath to search for
    :param namespaces: The namespaces to use
    :return: The text of the element found, or None
    :note: This function can only be used to parse the list of words
    """

    elements = node.findall(xPath, namespaces=namespaces)
    return [element.text for element in elements] if elements is not None else None


class Parser(object):
    def __init__(self, xml_path: AnyStr):
        self.xml_path = xml_path
        self.xml_namespace = "http://www.w3.org/XML/1998/namespace"
        self.tei_namespace = "http://www.tei-c.org/ns/1.0"
        self.etree = self._string_to_tree()
        self.artical = self.parse_artical()

    def parse_artical(self):
        return Artical(
            metadata=self._parse_metadata(),
            content=self._parse_content(),
            references=self._parse_reference(),
            authors=self._parse_author()
        )

    def _string_to_tree(self) -> ET.ElementTree:
        with open(self.xml_path, 'r') as xml_file:
            content = xml_file.read()
        if isinstance(content, str):
            return ET.parse(io.StringIO(content))
        else:
            raise TypeError(f"Expected string, got {type(content)}")

    def _parse_metadata(self) -> Metadata:
        tei_root = self.etree.getroot()
        title = _find_text_single(tei_root,
                                  './/tei:titleStmt/tei:title[@level="a"]',
                                  namespaces={'tei': self.tei_namespace})
        doi = _find_text_single(tei_root,
                                './/tei:sourceDesc/tei:biblStruct/tei:idno[@type="DOI"]',
                                namespaces={'tei': self.tei_namespace})
        publisher = _find_text_single(tei_root,
                                      './/tei:publicationStmt/tei:publisher',
                                      namespaces={'tei': self.tei_namespace})
        published_date = _find_text_single(tei_root,
                                           './/tei:publicationStmt/tei:date[@type="published"]',
                                           namespaces={'tei': self.tei_namespace})
        journal = _find_text_single(tei_root,
                                    './/tei:sourceDesc/tei:biblStruct/tei:monogr/tei:title[@level="j"]',
                                    namespaces={'tei': self.tei_namespace})
        return Metadata(
            title=title,
            doi=doi,
            publisher=publisher,
            journal=journal,
            published_date=published_date
        )

    def _parse_content(self) -> Content:
        tei_root = self.etree.getroot()
        abstract = _find_text_paragraph(tei_root,
                                        './/tei:profileDesc/tei:abstract/tei:div',
                                        namespaces={'tei': self.tei_namespace})
        keywords = _find_words_list(tei_root,
                                    './/tei:profileDesc/tei:textClass/tei:keywords/tei:term',
                                    namespaces={'tei': self.tei_namespace})
        return Content(
            abstract=abstract,
            keywords=keywords
        )

    def _parse_author(self) -> list[Author]:
        # Parse the XML string into an ElementTree object.
        tree = self.etree.getroot()
        authors = []

        # Find all author elements.
        author_elements = tree.findall('.//tei:sourceDesc/tei:biblStruct/tei:analytic/tei:author', namespaces={'tei': self.tei_namespace})

        for author_elem in author_elements:
            # Extract forenames (including middle name) and surname for each author.
            forenames = author_elem.findall('.//tei:persName/tei:forename', namespaces={'tei': self.tei_namespace})
            forename_texts = [forename.text for forename in forenames]
            surname = author_elem.find('.//tei:persName/tei:surname', namespaces={'tei': self.tei_namespace}).text

            # Combine forenames and surname into a full name.
            full_name = f"{' '.join(forename_texts)} {surname}"

            affiliation_element = author_elem.find('.//tei:affiliation/tei:orgName', namespaces={'tei': self.tei_namespace})
            affiliation = affiliation_element.text if affiliation_element is not None else None
            email_element = author_elem.find('.//tei:email', namespaces={'tei': self.tei_namespace})
            email = email_element.text if email_element is not None else None

            # Create an Author dataclass and add it to the list.
            authors.append(Author(name=full_name, affiliation=affiliation, email=email))

        return authors

    def _find_raw_reference(self, ns=None):
        print("extracting raw reference")
        if ns is None:
            ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
        tree = ET.parse(self.xml_path)
        root = tree.getroot()
        raw_references = []
        for note in root.findall('.//tei:note[@type="raw_reference"]', ns):
            ref = note.text
            ref = ref.replace('Ű', '-')
            ref = ref.replace('&apos;', "'")
            cleaned_ref = re.sub(r'-\s*', '-', ref)
            raw_references.append(cleaned_ref)
        print(raw_references[1])
        return raw_references

    def _store_references(self, raw_references):
        # Write the references to a temporary file
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
            # Each reference on a new line
            tmp.write('\n'.join(raw_references))
            tmp_path = tmp.name

        # Define the command to call Anystyle with the appropriate options
        # This command assumes Anystyle CLI is installed and `anystyle` is in your PATH
        cmd = ['anystyle', '-f', 'json', 'parse', tmp_path]

        try:
            # Run the Anystyle command （synchronously）
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            # Parse the JSON output
            parsed_references = json.loads(result.stdout)
            return parsed_references

        except subprocess.CalledProcessError as e:
            # Handle errors in the subprocess
            print(f"An error occurred while running Anystyle: {e}")
            return None

        finally:
            # Remove the temporary file
            subprocess.run(['rm', tmp_path])

    def _parse_reference(self):
        raw_references = self._find_raw_reference()
        stored_json_references = self._store_references(raw_references)
        if stored_json_references:
            return [
                Reference(
                    authors=ref.get('author', []),
                    title=''.join(ref.get('title', '')) if isinstance(ref.get('title'), list) else ref.get('title', ''),
                    type=ref.get('type', ''),
                    container_title=ref.get('container-title', ''),
                    doi=ref.get('doi', ''),
                    published_date=ref.get('date', [])[0] if ref.get('data') else ''
                )
                for ref in stored_json_references
            ]
