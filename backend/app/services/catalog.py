import analysis
from pathlib import Path


def parse_xml_to_article():
    xml_dir = Path("app/data/xml")
    for xml_file_path in xml_dir.glob("*.xml"):
        # Define the path to the XML directory or file
        # xml_file_path = Path("app/data/xml/1-s2.0-S0022096520305142-main.xml")

        # Check if the file exists to avoid FileNotFoundError
        if not xml_file_path.is_file():
            print(f"File not found: {xml_file_path}")
            return

        try:
            # Parse the article from the XML file
            article = analysis.get_artical(str(xml_file_path))
            print(article)
        except Exception as e:
            # Handle parsing errors or other exceptions
            print(f"Error parsing the XML file: {e}")


# Call the function to parse the XML and extract article information
parse_xml_to_article()
