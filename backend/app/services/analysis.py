import Extractor.extractor as Extractor
import Parser.parser as Parser


if __name__ == "__main__":
    path = "../../data/Papers/3485847.pdf"
    extractor = Extractor.Extractor(path)
    artical = Parser.Parser(extractor.xml_path)
    print(artical.metadata)
    print(artical.content)
