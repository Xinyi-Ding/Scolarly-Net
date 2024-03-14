import analysis

# from Parser.types import Artical
# from models import ParseArticalVO

if __name__ == "__main__":
    analysis.process_articles("app/data/xml", "app/data/json")

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
