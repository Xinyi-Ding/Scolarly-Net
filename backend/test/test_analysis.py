import pytest
import json
from backend.app.services import analysis
from backend.app.services.Parser.types import Artical, Metadata, Content
from pathlib import Path


# Parse test case data
def _parse_test_case_artical_metadata(path: str) -> Metadata:
    """
    Parse the test case data for the article metadata.

    Args:
        path (str): The path to the test case data.
    
    Returns:
        Artical: The article metadata.
    """
    with open(path, "r") as file:
        data = json.load(file)
        return Metadata(
            title=data["title"],
            doi=data["doi"],
            journal=data["journal"],
            published_date=data["publish date"],
            publisher=data["publisher"]
        )


def _parse_test_case_artical_content(path: str) -> Content:
    """
    Parse the test case data for the article content.

    Args:
        path (str): The path to the test case data.

    Returns:
        Artical: The article content, including the abstract and keywords.
    """
    with open(path, "r") as file:
        data = json.load(file)
        return Content(
            abstract=data["abstract"],
            keywords=data["keywords"]
        )


# Test cases
def test_parse_artical_metadata():
    """
    Test the parsing of the article metadata.
    """
    json_dir = Path("test/test_data/JSON")
    for json_file in json_dir.glob("*.json"):
        # Load test case data from JSON file
        with open(json_file, 'r', encoding='utf-8') as f:
            test_case = json.load(f)

        # Assuming _parse_test_case_artical_metadata function is meant to load and parse the JSON test case
        # We directly loaded the JSON above, but you might need to adjust this depending on your actual implementation

        # Construct corresponding PDF file path from the JSON file name
        pdf_file_name = json_file.stem + ".pdf"
        pdf_path = Path("test/test_data/Papers") / pdf_file_name

        # Parse the article metadata
        xml_path = analysis.get_extracted_xml(str(pdf_path))
        article = analysis.get_artical(xml_path)

        # Assuming article.metadata should be compared with test_case
        # You might need to adjust this comparison based on how your metadata and test cases are structured
        assert test_case == article.metadata, f"Metadata mismatch for {json_file.name}"


# def test_parse_artical_content():
#     """
#     Test the parsing of the article content.
#     """
#     # Parse the test case data
#     test_case = _parse_test_case_artical_content("backend/test/test_data/article_content.json")
#     # Parse the article content
#     article = analysis.parse_artical_content("backend/test/test_data/article_content.html")
#     # Check the test case and the parsed article are the same
#     assert test_case == article
