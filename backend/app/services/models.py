from pydantic import BaseModel
from dataclasses import dataclass

"""
The data models for the extractor service.
"""

@dataclass
class Metadata:
    title: str
    doi: str
    publisher: str
    journal: str
    published_date: str

    def __repr__(self):
        return f"Title: {self.title}\nDOI: {self.doi}\nPublisher: {self.publisher}\nJournal: {self.journal}\nPublished Date: {self.published_date}"


@dataclass
class Content:
    abstract: str
    keywords: list

    def __repr__(self):
        return f"Abstract: {self.abstract}\nKeywords: {self.keywords}"
