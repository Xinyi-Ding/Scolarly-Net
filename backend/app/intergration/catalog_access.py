from backend.app.db.mongoengine_models import Article
from backend.app.services.models import ArticleVO


def create_article(article_data: ArticleVO) -> ArticleVO:
    """
    Create a new article in the catalog
    @param article_data: ArticleVO - The data for the new article
    @return: ArticleVO - The created article
    """
    # Create a new Article document and save it to MongoDB
    article = Article(**article_data.dict()).save()

    # Return the created article as a Pydantic model
    return ArticleVO.from_orm(article)


def get_article(article_id: int) -> ArticleVO | None:
    """
    Retrieve an article from the catalog by its ID
    @param article_id: int - The ID of the article
    @return: ArticleVO | None - The retrieved article or None if not found
    """
    article = Article.objects(id=article_id).first()
    if article:
        return ArticleVO.from_orm(article)
    else:
        return None


def update_article(article_id: int, article_update: ArticleVO) -> ArticleVO | None:
    """
    Update an article in the catalog
    @param article_id: int - The ID of the article to update
    @param article_update: ArticleVO - The updated data for the article
    @return: ArticleVO | None - The updated article or None if not found
    """
    # Update the Article document
    article = Article.objects(id=article_id).first()
    if article:
        article.update(**article_update.dict(exclude={'id'}, exclude_unset=True))
        article.reload()  # Refresh the document from the database
        return ArticleVO.from_orm(article)
    else:
        return None


def delete_article(article_id: int) -> bool:
    """
    Delete an article from the catalog by its ID
    @param article_id: int - The ID of the article to delete
    @return: bool - True if the article was deleted, False if not found
    """
    # Delete an Article document by its ID
    article = Article.objects(id=article_id).first()
    if article:
        article.delete()
        return True
    else:
        return False
