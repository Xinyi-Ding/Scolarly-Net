from .Grobid.grobid_client import GrobidClient
from pathlib import Path
import subprocess


class Extractor(object):
    def __init__(self, artical_path, grobid_server="http://10.1.0.10:8070"):
        self.pdf_file_path = artical_path
        self.xml_path = self.generate_xml_path(artical_path)
        self.grobid_server = grobid_server
        self.pdf_to_xml()

    def pdf_to_xml(self):
        """
        Convert the PDF file to XML using Grobid.

        Args:
        - pdf_file_path: The file path to the PDF file.

        Returns:
        - str: The file path to the XML file.
        """
        if not self._check_grobid_running():
            return

        client = GrobidClient(grobid_server=self.grobid_server,
                              batch_size=1000,
                              sleep_time=5,
                              timeout=1200,
                              coordinates=["persName", "figure", "ref", "biblStruct", "formula", "s", "note", "title"])

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
        with open(self.xml_path, "w", encoding="utf-8") as file:
            file.write(req[2])

    def _check_grobid_running(self):
        """
        Check if the Grobid service is running by making a request to the specified URL using curl.

        Args:
        - url: The URL to the Grobid service (default 'http://localhost:8070').

        Returns:
        - bool: True if Grobid is running, False otherwise.
        """
        try:
            # Use curl to make a request to the Grobid service and capture the HTTP status code
            result = subprocess.run(['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', self.grobid_server], capture_output=True,
                                    text=True)
            status_code = result.stdout.strip()

            # Check if the status code is 200 (OK)
            if status_code == "200":
                print("Grobid service is running.")
                return True
            # If the status code is not 200, the service might not be running
            else:
                print(f"Grobid service might not be running. HTTP status code: {status_code}")
                return False
        except subprocess.CalledProcessError as e:
            # If an error occurs, the service is not running
            print(f"Failed to check Grobid service with curl: {e}")
            return False

    def generate_xml_path(self, pdf_file_path):
        pdf_path = Path(pdf_file_path)
        pdf_dir = str(pdf_path.parent)
        xml_dir = pdf_dir.replace("Papers", "xml")
        xml_file_path = Path(xml_dir) / (pdf_path.stem + ".xml")
        return str(xml_file_path)
