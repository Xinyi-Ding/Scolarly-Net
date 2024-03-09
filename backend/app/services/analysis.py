from Extractor import extractor as Extractor
from Parser import parser as Parser
from pathlib import Path


if __name__ == "__main__":
    path = "../data/xml/test3.xml"
    parser = Parser.Parser(path)
    artical = parser.artical
    print(artical.metadata)
    print(artical.content)
