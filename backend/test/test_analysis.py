import json
from backend.app.services import analysis
<<<<<<< HEAD
from backend.app.services.Parser.types import Reference
=======
from backend.app.services.Parser.types import Metadata, Content
>>>>>>> main
from pathlib import Path
from difflib import SequenceMatcher


# Test cases for the article metadata
def normalize_text(text):
    """
    Normalize the text by converting it to lowercase and removing extra whitespaces.

    Args:
        text (str): The text to normalize.

    Returns:
        str: The normalized text.
    """
    return ' '.join(text.lower().split())


# Parse test case data
<<<<<<< HEAD
def _parse_test_case_artical_reference(path: str) -> Reference:
    with open(path, "r") as file:
        data = json.load(file)
        references = [
            Reference(
                authors=ref.get('author', []),
                title=ref.get('title', ''),
                type=ref.get('type', ''),
                container_title=ref.get('container-title', ''),
                doi=ref.get('doi', ''),
                published_date=ref.get('date', [])[0] if ref.get('data') else ''
            )
            for ref in data.get('references', [])
        ]
        print(references)
        return references
=======
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

>>>>>>> main

def are_similar(text1, text2, threshold=0.8):
    """
    Check if two texts are similar based on the Levenshtein distance.

    Args:
        text1 (str): The first text.
        text2 (str): The second text.
        threshold (float): The similarity threshold (default 0.9).

    Returns:
        bool: True if the texts are similar, False otherwise.
    """
    text1 = normalize_text(text1)
    text2 = normalize_text(text2)
    similarity = SequenceMatcher(None, text1, text2).ratio()
    return similarity >= threshold


<<<<<<< HEAD
# Test cases for the article reference
def test_parse_artical_reference():
    """
    Test the parsing of the article reference.
    """
    json_dir = Path("test/test_data/JSON")
    for json_file in json_dir.glob("*.json"):
        test_case = _parse_test_case_artical_reference(str(json_file))
=======
# Test cases for the article metadata
def test_parse_artical_metadata():
    """
    Test the parsing of the article metadata.
    """
    json_dir = Path("test/test_data/JSON")
    for json_file in json_dir.glob("*.json"):
        test_case = _parse_test_case_artical_metadata(str(json_file))
>>>>>>> main

        # Construct corresponding PDF file path from the JSON file name
        pdf_file_name = json_file.stem + ".pdf"
        pdf_path = Path("test/test_data/Papers") / pdf_file_name

        # Parse the article metadata
        xml_path = analysis.get_extracted_xml(str(pdf_path))
        article = analysis.get_artical(xml_path)
<<<<<<< HEAD
        assert are_similar(normalize_text(test_case.reference), normalize_text(article.references)), f"Reference mismatch for {json_file.name}"

=======
        assert test_case == article.metadata, f"Metadata mismatch for {json_file.name}"


# Test cases for the article content
def test_parse_artical_content():
    """
    Test the parsing of the article content.
    """
    json_dir = Path("test/test_data/JSON")
    for json_file in json_dir.glob("*.json"):
        test_case = _parse_test_case_artical_content(str(json_file))

        # Construct corresponding PDF file path from the JSON file name
        pdf_file_name = json_file.stem + ".pdf"
        pdf_path = Path("test/test_data/Papers") / pdf_file_name

        # Parse the article metadata
        xml_path = analysis.get_extracted_xml(str(pdf_path))
        article = analysis.get_artical(xml_path)
        assert are_similar(normalize_text(test_case.abstract),
                           normalize_text(article.content.abstract)), f"Abstract mismatch for {json_file.name}"
>>>>>>> main
