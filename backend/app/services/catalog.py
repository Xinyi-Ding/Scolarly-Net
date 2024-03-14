import json
import analysis
from pathlib import Path


# from Parser.types import Artical
# from models import ParseArticalVO


def parse_xml_to_article(xml_file_path):
    try:
        # Use the analysis module to parse the XML file into an Artical object
        article = analysis.get_artical(str(xml_file_path))
        return article  # Return the Artical object if parsing is successful
    except Exception as e:
        # Handle any exceptions that might occur during parsing
        print(f"Error parsing the XML file: {e}")
        return None  # Return None in case of an exception


def store_article_as_json(article, json_file_path):
    # Convert the Artical object to a dictionary
    article_dict = article.to_dict()  # Assuming to_value_object() provides the dictionary representation
    # Write the dictionary to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(article_dict, json_file, indent=4)


def main():
    xml_dir = Path("app/data/xml")
    json_dir = Path("app/data/json")  # Define the path to the JSON directory
    json_dir.mkdir(parents=True, exist_ok=True)  # Ensure the JSON directory exists

    for xml_file_path in xml_dir.glob("*.xml"):
        # Check if the file exists to prevent a FileNotFoundError
        if not xml_file_path.is_file():
            print(f"File not found: {xml_file_path}")
            continue  # Skip to the next file if the current file doesn't exist

        article = parse_xml_to_article(xml_file_path)
        if article:  # Check if the returned object is not None
            # Define the path for the JSON file (same name as the XML file but with .json extension)
            json_file_name = xml_file_path.stem + '.json'  # Use stem to get the file name without suffix
            json_file_path = json_dir / json_file_name  # Construct the full path for the JSON file

            # Store the article as a JSON file
            store_article_as_json(article, json_file_path)


if __name__ == "__main__":
    main()

# def parse_xml_to_article():
#     # Define the path to the XML file
#     xml_file_path = Path("app/data/xml/1-s2.0-S0022096520305142-main.xml")
#
#     # Check if the file exists to prevent a FileNotFoundError
#     if not xml_file_path.is_file():
#         print(f"File not found: {xml_file_path}")
#         return None  # Return None if the file doesn't exist
#
#     try:
#         # Use the analysis module to parse the XML file into an Artical object
#         article = analysis.get_artical(str(xml_file_path))
#         return article  # Return the Artical object if parsing is successful
#     except Exception as e:
#         # Handle any exceptions that might occur during parsing
#         print(f"Error parsing the XML file: {e}")
#         return None  # Return None in case of an exception
#
# # Call the function to parse the XML and check if a valid Artical object is returned
# article = parse_xml_to_article()
# if article:  # Check if the returned object is not None
#     adict = article.to_dict()  # Convert the Artical object to a value object (VO)
#     print(adict)  # Print the value object to inspect its content
#     vo = ParseArticalVO(**adict)  # Create a ParseArticalVO object from the value object (VO
#     print("------------------")
#     print(vo)
# else:
#     print("No valid article was returned.")
