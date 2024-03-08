from .types import Metadata, Content
import grobid_tei_xml


class Parser(object):
    def __init__(self, xml_path):
        self.xml_path = xml_path
        self.metadata = None
        self.content = None

    def parse_metadata(self):
        with open(self.xml_path, 'r') as xml_file:
            doc = grobid_tei_xml.parse_document_xml(xml_file.read())
        self.metadata = Metadata(
            title=doc.header.title,
            doi=doc.header.doi,
            publisher=doc.header.publisher,
            journal=doc.header.journal,
            published_date=doc.header.date
        )

    def parse_content(self):
        with open(self.xml_path, 'r') as xml_file:
            doc = grobid_tei_xml.parse_document_xml(xml_file.read())
        self.content = Content(
            abstract=doc.abstract,
            keywords=[" "]
        )
