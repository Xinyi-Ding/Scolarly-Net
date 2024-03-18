import json
from pathlib import Path

from .Extractor.extractor import Extractor
from .Parser.parser import Parser
from .Parser.types import ArticleObject
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
from gensim import corpora, models
from gensim.models import Phrases
from gensim.models.phrases import Phraser
import string
import re


def _clean_doc(doc):
    """
    Cleans the document by removing stop words, punctuation, and lemmatizing the words.

    Args:
        doc (str): The document text to clean.

    Returns:
        str: The cleaned document text.
    """
    # Download the NLTK resources
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)

    stop = set(stopwords.words('english'))
    exclude = set(string.punctuation)
    lemma = WordNetLemmatizer()
    doc_no_numbers = re.sub(r'\b\d+(\.\d+)?', '', doc)
    stop_free = " ".join([i for i in doc_no_numbers.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    cleaned = re.sub(r'[^\w\s-]', '', punc_free)
    normalized = " ".join(lemma.lemmatize(word) for word in cleaned.split())
    tagged = pos_tag(normalized.split())

    nouns_and_adjectives = " ".join(
        word for word, tag in tagged if tag in ('NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS'))

    return nouns_and_adjectives


def _clean_abstract(abstract):
    """
    Cleans the abstract text by removing newlines, arrows, and combining numbers with periods.

    Args:
        abstract (str): The abstract text to clean.

    Returns:
        str: The cleaned abstract text.
    """
    formatted_numbers = re.sub(r'(\d+)\.\s+(\d+)', r'\1.\2', abstract)
    replace_newlines_arrows = re.sub(r'\n|→|↵', ' ', formatted_numbers)
    cleaned_text = re.sub(r'(\w+)-\s+(\w+)', r'\1\2', replace_newlines_arrows)
    return cleaned_text


def get_topics_from_article(article: ArticleObject) -> list:
    """
    Extracts unique keywords that represent topics from a given article using LDA.

    Args:
        article (object): An article object with 'metadata' and 'content' attributes.

    Returns:
        list: A list of unique keywords representing the topics.
    """
    # Combine the article's title, abstract, and keywords into a single list
    docs = [
        article.metadata.title,
        article.content.abstract,
        " ".join(article.content.keywords)
    ]

    # Preprocess each document
    doc_clean = [_clean_doc(_clean_abstract(doc)).split() for doc in docs]

    # Identify bigrams using the gensim's Phrases model
    phrases = Phrases(doc_clean, min_count=5, threshold=10)  # Adjust parameters as needed
    bigram = Phraser(phrases)

    # Apply the identified bigrams to the processed docs
    docs_phrased = [bigram[doc] for doc in doc_clean]

    # Create a dictionary and a corpus for LDA analysis
    dictionary = corpora.Dictionary(docs_phrased)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in docs_phrased]

    # Perform LDA topic modeling
    Lda = models.ldamodel.LdaModel(
        corpus=doc_term_matrix,
        num_topics=5,
        id2word=dictionary,
        passes=500,
        random_state=42
    )

    # Extract the top 3 keywords from each topic and replace underscores with spaces
    topics = Lda.show_topics(num_topics=-1, num_words=5, formatted=False)
    unique_keywords = set()
    for _, topic_keywords in topics:
        keywords = [" ".join(word.split('_')) for word, _ in topic_keywords]
        unique_keywords.update(keywords)

    # Convert the set of unique keywords to a list for output
    topic_list = list(unique_keywords)
    filtered_keywords = [word for word in topic_list
                         if not ((len(word) == 1) and (word.isdigit() or word.isalpha()))]
    return filtered_keywords


def get_article_object(xml_path) -> ArticleObject:
    """
    Parses the XML file into an ArticleObject and extracts topics from the article.

    Args:
        xml_path (str): The path to the XML file.

    Returns:
        ArticleObject: The parsed article object with extracted topics.
    """
    parser = Parser(xml_path)
    article = parser.article
    article.content.keywords = get_topics_from_article(article)
    article.content.abstract = _clean_abstract(article.content.abstract)
    return article


def get_extracted_xml(pdf_path, grobid_server="http://10.1.0.10:8070") -> str:
    """
    Extracts the XML file from the PDF using GROBID.

    Args:
        pdf_path (str): The path to the PDF file.
        grobid_server (str): The URL of the GROBID server.

    Returns:
        str: The path to the extracted XML file.
    """
    extractor = Extractor(pdf_path, grobid_server=grobid_server)

    return extractor.xml_path


def parse_xml_to_article(xml_file_path):
    """
    Parses the XML file into an ArticleObject.

    Args:
        xml_file_path (str): The path to the XML file.

    Returns:
        ArticleObject: The parsed article object.
    """
    try:
        # Use the analysis module to parse the XML file into an Artical object
        article = get_article_object(str(xml_file_path))
        return article  # Return the Artical object if parsing is successful
    except Exception as e:
        # Handle any exceptions that might occur during parsing
        print(f"Error parsing the XML file: {e}")
        return None  # Return None in case of an exception


def store_article_as_json(article, json_file_path):
    """
    Stores the ArticleObject as a JSON file.

    Args:
        article (ArticleObject): The article object to store.
        json_file_path (str): The path to the JSON file.

    Returns:
        None
    """
    # Convert the Artical object to a dictionary
    article_dict = article.to_dict()  # Assuming to_value_object() provides the dictionary representation
    # Write the dictionary to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(article_dict, json_file, indent=4)


def process_articles(xml_dir: str, json_dir: str):
    """
    Processes the XML files in the specified directory and stores the parsed articles as JSON files.

    Args:
        xml_dir (str): The path to the directory containing the XML files.
        json_dir (str): The path to the directory where the JSON files will be stored.

    Returns:
        None
    """
    xml_dir = Path(xml_dir)
    json_dir = Path(json_dir)
    json_dir.mkdir(parents=True, exist_ok=True)

    for xml_file_path in xml_dir.glob("*.xml"):
        if not xml_file_path.is_file():
            print(f"File not found: {xml_file_path}")
            continue

        article = parse_xml_to_article(str(xml_file_path))
        if article:
            json_file_name = xml_file_path.stem + '.json'
            json_file_path = json_dir / json_file_name
            store_article_as_json(article, str(json_file_path))
