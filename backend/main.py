from app.services import analysis
from app.services.Parser.types import Artical, Metadata, Content, Reference, Author

artical = analysis.get_artical(analysis.get_extracted_xml("app/data/Papers/3418094.3418142.pdf", grobid_server="http://localhost:8070"))
print(artical.authors)
