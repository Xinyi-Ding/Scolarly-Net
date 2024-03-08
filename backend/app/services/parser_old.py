import xml.etree.ElementTree as ET
import grobid_tei_xml
from prettytable import PrettyTable


def parse_document(xml_path):
    with open(xml_path, 'r') as xml_file:
        return grobid_tei_xml.parse_document_xml(xml_file.read())


def create_title_table(doc):
    title_table = PrettyTable()
    title_table.field_names = ["Title", "DOI", "Publisher", "Journal", "Published Date"]
    title_table.add_row([doc.header.title, doc.header.doi, doc.header.publisher, doc.header.journal, doc.header.date])
    return title_table


def create_author_table(doc):
    author_table = PrettyTable()
    author_table.field_names = ["Authors", "Affiliation", "Email"]
    for author in doc.header.authors:
        author_table.add_row(
            [author.full_name, author.affiliation, author.email])
    return author_table


def create_citation_table(doc):
    citation_table = PrettyTable()
    citation_table.field_names = ["Cited Title", "Author", "Published Date"]
    for citation in doc.citations:
        citation_table.add_row([citation.title, [c.full_name for c in citation.authors], citation.date])
    return citation_table


def extract_keywords(xml_path, ns=None):
    if ns is None:
        ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
    tree = ET.parse(xml_path)
    root = tree.getroot()
    return [keyword.text for keyword in root.findall(".//tei:keywords", ns)]


if __name__ == '__main__':

    xml_path = "data/xml/Visual exploration of color usage in Vincent van Gogh's Paintings.xml"
    doc = parse_document(xml_path)

    title_table = create_title_table(doc)
    author_table = create_author_table(doc)
    citation_table = create_citation_table(doc)
    keywords = extract_keywords(xml_path)

    # print(title_table)
    # print(author_table)
    # print(citation_table)
    print("Keywords:", keywords)
