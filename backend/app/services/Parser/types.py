from dataclasses import dataclass

from typing import List

"""
The data models for the Parser service.
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

@dataclass
class Reference:
    authors: list
    title: str
    type: str
    container_title: str
    doi: str
    published_date: str

    def __repr__(self):
        return (f"Authors: {self.authors}\n"
                f"Title: {self.title}\n"
                f"Type: {self.type}\n"
                f"Container Title: {self.container_title}\n"
                f"DOI: {self.doi}\n"
                f"Published Date: {self.published_date}\n")

    def __eq__(self, other):
        if not isinstance(other, Reference):
            return False
        return self.title == other.title and \
            self.doi == other.doi and \
            self.authors == other.authors and \
            self.type == other.type and \
            self.container_title == other.container_title and \
            self.published_date == other.published_date
@dataclass
class Artical:
    metadata: Metadata
    content: Content
    references: List[Reference]

    def __repr__(self):
        return f"Metadata: {self.metadata}\n" \
               f"Content: {self.content}\n" \
               f"References: {self.references}"