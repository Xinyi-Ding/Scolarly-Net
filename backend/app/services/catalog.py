import json
import os
from pathlib import Path

from backend.app.intergration.catalog_access import ArticleCRUD, AuthorCRUD, ArticleAuthorCRUD, \
    ArticleCitationCRUD, TopicCRUD, ArticleTopicCRUD

from models import ParseArticalVO, ArticleVO, AuthorVO, ArticleAuthorVO, ArticleCitationVO, AuthorFilter, \
    ArticleFilter, ArticleAuthorFilter, TopicFilter, TopicVO, ArticleTopicVO, ArticleCitationFilter

from Parser.types import Artical


def save_parse_article(parse_article: ParseArticalVO | dict | Artical):
    """
    This function processes and saves the article metadata, authors, references, and topics to the database.
    :param parse_article: A ParseArticleVO, dict,
    or Artical instance containing the article metadata, authors, references, and topics.
    :return: None
    """

    # Type checking and conversion
    if isinstance(parse_article, ParseArticalVO):
        # If the input is already a ParseArticleVO instance, use it directly
        parse_article_vo = parse_article
    elif isinstance(parse_article, dict):
        parse_article_vo = ParseArticalVO.from_dict(parse_article)
    elif isinstance(parse_article, Artical):
        parse_article_vo = ParseArticalVO.from_dict(parse_article.to_dict())
    else:
        raise ValueError("Unsupported type for parse_article_vo")

    # Initialize CRUD operation classes
    article_crud = ArticleCRUD()
    author_crud = AuthorCRUD()
    article_author_crud = ArticleAuthorCRUD()
    article_citation_crud = ArticleCitationCRUD()
    topic_crud = TopicCRUD()
    article_topic_crud = ArticleTopicCRUD()

    if not article_crud.get_by_filter(ArticleFilter(doi=parse_article_vo.metadata.doi)):
        # Process and save the article metadata
        article_data = ArticleVO(
            title=parse_article_vo.metadata.title,
            abstract=parse_article_vo.content.abstract,
            publisher=parse_article_vo.metadata.publisher,
            date=parse_article_vo.metadata.published_date,
            doi=parse_article_vo.metadata.doi,
            container_title=parse_article_vo.metadata.journal
        )

        try:
            # Save the article to the database
            saved_article = article_crud.create(article_data)
        except Exception as e:
            print(f"Error saving article: {e}")
            return  # or handle error accordingly

        # Process and save authors with their affiliations
        for parse_author_vo in parse_article_vo.authors:
            # Check if the author already exists in the database
            author_vo_list = author_crud.get_by_filter(
                AuthorFilter(name=parse_author_vo.name, email=parse_author_vo.email))
            if author_vo_list:
                # If the author exists, use the existing author
                saved_author = author_vo_list[0]
            else:
                # If the author does not exist, save the author
                try:
                    saved_author = author_crud.create(AuthorVO(name=parse_author_vo.name, email=parse_author_vo.email))
                except Exception as e:
                    print(f"Error saving author: {e}")
                    continue  # or handle error accordingly

            # Associate the author with the saved article
            if not article_author_crud.get_by_filter(ArticleAuthorFilter(article_id=saved_article.article_id,
                                                                         author_id=saved_author.author_id)):
                try:
                    article_author_crud.create(
                        ArticleAuthorVO(article_id=saved_article.article_id, author_id=saved_author.author_id))
                except Exception as e:
                    print(f"Error creating article-author relationship: {e}")
                    # Decide whether to continue or handle differently

            # Process and save the author's affiliation (Future work)

        # Process and save references (as articles) and create citation relationships
        for parse_reference_vo in parse_article_vo.references:
            # Check if the reference already exists in the database
            reference_article_lst = article_crud.get_by_filter(
                ArticleFilter(title=parse_reference_vo.title, doi=parse_reference_vo.doi))

            if reference_article_lst:
                reference_article = reference_article_lst[0]
            else:
                article_vo = ArticleVO(
                    title=parse_reference_vo.title,
                    doi=parse_reference_vo.doi,
                    date=parse_reference_vo.published_date,
                    container_title=parse_reference_vo.container_title[
                        0] if parse_reference_vo.container_title else None
                )
                try:
                    reference_article = article_crud.create(article_vo)
                except Exception as e:
                    print(f"Error saving reference article: {e}")
                    continue  # or handle error accordingly

            try:
                if not article_citation_crud. \
                        get_by_filter(ArticleCitationFilter(citing_article_id=saved_article.article_id,
                                                            cited_article_id=reference_article.article_id)):
                    article_citation_crud.create(ArticleCitationVO(citing_article_id=saved_article.article_id,
                                                                   cited_article_id=reference_article.article_id))
            except Exception as e:
                print(f"Error creating article citation: {e}")
                # Decide whether to continue or handle differently

        # Process and save topics and create relationships between articles and topics
        for keyword in parse_article_vo.content.keywords:
            topic_vo = topic_crud.get_by_filter(TopicFilter(name=keyword))
            if topic_vo:
                topic_vo = topic_vo[0]
            else:
                try:
                    topic_vo = topic_crud.create(TopicVO(name=keyword))
                except Exception as e:
                    print(f"Error saving topic: {e}")
                    continue  # or handle error accordingly

            try:
                article_topic_crud.create(
                    ArticleTopicVO(article_id=saved_article.article_id, topic_id=topic_vo.topic_id))
            except Exception as e:
                print(f"Error creating article-topic relationship: {e}")
                # Decide whether to continue or handle differently


def save_parse_articles_within_dir(folder_path):
    """
    Recursively processes each JSON file in a given folder and its subfolders.
    :param folder_path: The path to the folder containing JSON files to process.
    :return: None
    """
    # Traverse all files and subdirectories within the given folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file is a JSON file based on its extension
            if Path(file).suffix == '.json':
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                try:
                    # Open the JSON file and load its content
                    with open(file_path, 'r', encoding='utf-8') as f:
                        parse_article_vo = ParseArticalVO.from_dict(json.load(f))
                    # Call the function to process the parsed article object
                    save_parse_article(parse_article_vo)
                except Exception as e:
                    # Print an error message if something goes wrong
                    print(f"Error processing file {file_path}: {e}")


def main():
    # Example usage
    folder_path = r'C:\Users\Qiu\Desktop\frame\Carlson-Johnson\backend\app\data\json'
    # Process all JSON files within the given folder and its folders
    save_parse_articles_within_dir(folder_path)

    # analysis.process_articles("app/data/xml", "app/data/json")


if __name__ == "__main__":
    main()
