import json
from typing import List
from backend.app.services import analysis
from backend.app.services.Parser.types import Metadata, Content, Reference
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
def _parse_test_case_artical_reference(path: str) -> List[Reference]:
    with open(path, "r") as file:
        data = json.load(file)
        if not data['Reference']:
            return []
        return [
            Reference(
                authors=ref.get('authors', ''),
                title=ref.get('title', ''),
                type=ref.get('type', ''),
                container_title=ref.get('container-title', ''),
                doi=ref.get('doi', ''),
                published_date=ref.get('date', [])[0] if ref.get('data') else ''
            )
            for ref in data['Reference']
        ]


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

def _are_reference_similar(reference1: List[Reference], reference2: List[Reference], match_threshold=0.8, match_ratio_threshold=0.5):
    """
    Check if the extracted references (reference2) are accurate compared to the manually extracted references (reference1).
    Allows for differences in length and some level of inaccuracy in reference2.

    Args:
        reference1 (List[Reference]): The manually extracted references for comparison.
        reference2 (List[Reference]): The automatically extracted references to be tested.
        match_threshold (float): The similarity threshold for considering two references as a match.
        match_ratio_threshold (float): The minimum ratio of reference1 that must find a match in reference2 for the function to return True.

    Returns:
        bool: True if the accuracy of reference2 is deemed acceptable, False otherwise.
    """
    if len(reference1) == 0 and len(reference2) == 0:
        return True
    match_count = 0

    for ref1 in reference1:
        for ref2 in reference2:
            # Compute similarity based on titles, but other fields like authors and DOI can also be considered
            title_similarity = SequenceMatcher(None, normalize_text(ref1.title), normalize_text(ref2.title)).ratio()
            if title_similarity > match_threshold:
                match_count += 1
                break  # Stop searching once a match is found for this reference

    # Check if the ratio of matched references in reference1 is above the threshold

    match_ratio = match_count / len(reference1)
    print("match ratio:", match_ratio)
    return match_ratio >= match_ratio_threshold

# Test cases for the article reference
def test_parse_artical_reference():
    """
    Test the parsing of the article reference.
    """
    json_dir = Path("test/test_data/JSON")
    for json_file in json_dir.glob("*.json"):
        print("testing reference:", json_file.name)
        test_case = _parse_test_case_artical_reference(str(json_file))
        # Construct corresponding PDF file path from the JSON file name
        pdf_file_name = json_file.stem + ".pdf"
        pdf_path = Path("test/test_data/Papers") / pdf_file_name

        # Parse the article metadata
        xml_path = analysis.get_extracted_xml(str(pdf_path))
        article = analysis.get_artical(xml_path)
        # print("reference test case")
        # print(test_case)
        # print(article.references)
        assert _are_reference_similar(test_case, article.references), f"Reference mismatch for {json_file.name}"

# Test cases for the article metadata
def test_parse_artical_metadata():
    """
    Test the parsing of the article metadata.
    """
    json_dir = Path("test/test_data/JSON")
    for json_file in json_dir.glob("*.json"):
        test_case = _parse_test_case_artical_metadata(str(json_file))

        # Construct corresponding PDF file path from the JSON file name
        pdf_file_name = json_file.stem + ".pdf"
        pdf_path = Path("test/test_data/Papers") / pdf_file_name

        # Parse the article metadata
        xml_path = analysis.get_extracted_xml(str(pdf_path))
        article = analysis.get_artical(xml_path)
        print(test_case.journal)
        print(article.metadata.journal)
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
        # print(test_case)
        # print(article.content.abstract)
        assert are_similar(normalize_text(test_case.abstract),
                           normalize_text(article.content.abstract)), f"Abstract mismatch for {json_file.name}"
