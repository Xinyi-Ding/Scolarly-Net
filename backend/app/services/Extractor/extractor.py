from .Grobid.grobid_client import GrobidClient
from pathlib import Path


class Extractor(object):
    def __init__(self, artical_path):
        self.pdf_file_path = artical_path
        self.xml_path = None
        self.pdf_to_xml()

    def pdf_to_xml(self):
        config_path = Path.cwd()/"Extractor/Grobid/config.json"
        client = GrobidClient(config_path=config_path)

        req = client.process_pdf(
            service="processFulltextDocument",
            pdf_file=self.pdf_file_path,
            generateIDs=True,
            consolidate_header=True,
            consolidate_citations=True,
            include_raw_citations=True,
            include_raw_affiliations=True,
            tei_coordinates=True,
            segment_sentences=True
        )

        self.xml_path = f"../data/xml/test3.xml"
        with open(self.xml_path, "w", encoding="utf-8") as file:
            file.write(req[2])
