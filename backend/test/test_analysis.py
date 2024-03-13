import json
from typing import List
from backend.app.services import analysis
from backend.app.services.Parser.types import Metadata, Content, Reference, Author
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
        return [
            Reference(
                authors=ref.get('author', []),
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


def _parse_test_case_artical_authors(path: str) -> List[Author]:
    """
    Parse the test case data for the article authors.

    Args:
        path (str): The path to the test case data.

    Returns:
        List[Author]: The list of authors.
    """
    with open(path, "r") as file:
        data = json.load(file)
        return [
            Author(
                name=author.get('name', ''),
                affiliation=author.get('affiliation', ''),
                email=author.get('email', '')
            )
            for author in data['authors']
        ]


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


def _are_reference_similar(reference1: List[Reference], reference2: List[Reference]):
    """
    Check if two lists of references are similar based on their titles.
    A reference is considered similar to another if their titles have more than 80% similarity.
    References in one list are matched to the most similar
    references in the other list without assuming identical order.

    Args:
        reference1 (List[Reference]): The first list of references.
        reference2 (List[Reference]): The second list of references.

    Returns:
        bool: True if the references are considered similar, False otherwise.
    """
    # Ensure reference1 is always the longer list for simplicity
    if len(reference1) < len(reference2):
        reference1, reference2 = reference2, reference1

    # Initialize a list to keep track of which references in the longer list have been matched
    matched = [False] * len(reference1)

    for ref2 in reference2:
        best_match_index = -1
        best_similarity = 0.8  # Set to the threshold to ensure only better matches are considered
        for i, ref1 in enumerate(reference1):
            if not matched[i]:  # Only consider unmatched references
                similarity = SequenceMatcher(None, normalize_text(ref1.title), normalize_text(ref2.title)).ratio()
                if similarity > best_similarity:
                    best_similarity = similarity
                    best_match_index = i

        if best_match_index >= 0:
            matched[best_match_index] = True  # Mark this reference as matched
        else:
            return False  # If no match found for a reference in the shorter list, return False

    return True


# @TODO Test cases for the article reference
# def test_parse_artical_reference():
#     """
#     Test the parsing of the article reference.
#     """
#     json_dir = Path("test/test_data/JSON")
#     for json_file in json_dir.glob("*.json"):
#         test_case = _parse_test_case_artical_reference(str(json_file))
#         # Construct corresponding PDF file path from the JSON file name
#         pdf_file_name = json_file.stem + ".pdf"
#         pdf_path = Path("test/test_data/Papers") / pdf_file_name
#
#         # Parse the article metadata
#         xml_path = analysis.get_extracted_xml(str(pdf_path))
#         article = analysis.get_artical(xml_path)
#         assert _are_reference_similar(test_case, article.references), f"Reference mismatch for {json_file.name}"


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


# Test cases for the article authors
def test_parse_artical_authors():
    """
    Test the parsing of the article authors.
    """
    json_dir = Path("test/test_data/JSON")
    for json_file in json_dir.glob("*.json"):
        test_case = _parse_test_case_artical_authors(str(json_file))

        # Construct corresponding PDF file path from the JSON file name
        pdf_file_name = json_file.stem + ".pdf"
        pdf_path = Path("test/test_data/Papers") / pdf_file_name

        # Parse the article metadata
        xml_path = analysis.get_extracted_xml(str(pdf_path))
        article = analysis.get_artical(xml_path)
        for i, author in enumerate(article.authors):
            assert test_case[i].name == author.name, f"Author mismatch for {json_file.name}"
