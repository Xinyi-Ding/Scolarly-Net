from dataclasses import dataclass, asdict
from typing import Optional
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
        return f"Title: {self.title}\n" \
               f"DOI: {self.doi}\n" \
               f"Publisher: {self.publisher}\n" \
               f"Journal: {self.journal}\n" \
               f"Published Date: {self.published_date}"

    def __eq__(self, other):
        if not isinstance(other, Metadata):
            return False
        return self.title.lower() == other.title.lower() and \
            self.doi == other.doi and \
            self.publisher == other.publisher and \
            self.journal == other.journal and \
            self.published_date == other.published_date

    def to_json(self):
        return {
            "title": self.title,
            "doi": self.doi,
            "publisher": self.publisher,
            "journal": self.journal,
            "published_date": self.published_date
        }


@dataclass
class Content:
    abstract: str
    keywords: list

    def __repr__(self):
        return f"Abstract: {self.abstract}\n" \
               f"Keywords: {self.keywords}\n"

    def __eq__(self, other):
        if not isinstance(other, Content):
            return False
        return self.abstract == other.abstract and self.keywords == other.keywords

    def to_json(self):
        return {
            "abstract": self.abstract,
            "keywords": self.keywords
        }


@dataclass
class Author:
    name: str
    affiliation: str
    email: Optional[str]

    def __repr__(self):
        return (f"Name: {self.name}\n"
                f"Affiliation: {self.affiliation}\n"
                f"Email: {self.email}\n")

    def __eq__(self, other):
        if not isinstance(other, Author):
            return False
        return self.name == other.name and self.affiliation == other.affiliation and self.email == other.email

    def to_json(self):
        return {
            "name": self.name,
            "affiliation": self.affiliation,
            "email": self.email
        }


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
class ArticleObject:
    metadata: Metadata
    content: Content
    authors: List[Author]
    references: List[Reference]

    def __repr__(self):
        return (f"Metadata: {self.metadata}\n"
                f"Content: {self.content}\n"
                f"Authors: {self.authors}\n"
                f"References: {self.references}")

    def to_dict(self):
        return asdict(self)

    def to_json(self):
        return {
            "metadata": self.metadata.to_json(),
            "content": self.content.to_json(),
            "authors": [author.to_json() for author in self.authors],
            "references": len(self.references)
        }
