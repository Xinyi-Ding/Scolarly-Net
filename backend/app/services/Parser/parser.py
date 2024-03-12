import io

from .types import Metadata, Content, Artical
from typing import AnyStr, Dict, List, Optional
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


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
            content=self._parse_content()
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
        title = _find_text_single(tei_root, './/tei:titleStmt/tei:title[@level="a"]', namespaces={'tei': self.tei_namespace})
        doi = _find_text_single(tei_root, './/tei:sourceDesc/tei:biblStruct/tei:idno[@type="DOI"]', namespaces={'tei': self.tei_namespace})
        publisher = _find_text_single(tei_root, './/tei:publicationStmt/tei:publisher', namespaces={'tei': self.tei_namespace})
        published_date = _find_text_single(tei_root, './/tei:publicationStmt/tei:date[@type="published"]', namespaces={'tei': self.tei_namespace})
        journal = _find_text_single(tei_root, './/tei:sourceDesc/tei:biblStruct/tei:monogr/tei:title[@level="j"]', namespaces={'tei': self.tei_namespace})
        return Metadata(
            title=title,
            doi=doi,
            publisher=publisher,
            journal=journal,
            published_date=published_date
        )

    def _parse_content(self) -> Content:
        tei_root = self.etree.getroot()
        abstract = _find_text_paragraph(tei_root, './/tei:profileDesc/tei:abstract/tei:div', namespaces={'tei': self.tei_namespace})
        keywords = _find_words_list(tei_root, './/tei:profileDesc/tei:textClass/tei:keywords/tei:term', namespaces={'tei': self.tei_namespace})
        return Content(
            abstract=abstract,
            keywords=keywords
        )
