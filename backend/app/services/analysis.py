# from Extractor import extractor as Extractor
# from Parser import parser as Parser
# from pathlib import Path
#
# if __name__ == "__main__":
#     # print(Path.cwd())
#     path = "../data/Papers/2629451.pdf"
#     extractor = Extractor.Extractor(path)
#     artical = Parser.Parser(extractor.xml_path)
#     # print(artical.metadata)
#     # print(artical.content)
#     print(artical.references)

from .Extractor import extractor as Extractor
from .Parser import parser as Parser
from .Parser.types import Artical
from pathlib import Path


def get_artical(xml_path) -> Artical:
    parser = Parser.Parser(xml_path)
    artical = parser.artical
    return artical


def get_extracted_xml(pdf_path) -> str:
    extractor = Extractor.Extractor(pdf_path)
    return extractor.xml_path



def get_article_reference(article):
    """
    Print the metadata, content, and references of the given article.

    Parameters:
    - article (Parser object): The article object from which to extract details.
    """
    # Uncomment the lines below if you want to print metadata and content as well
    # print("Metadata:", article.metadata)
    # print("Content:", article.content)
    return article.references

