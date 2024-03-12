from dataclasses import dataclass

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
        return self.title == other.title and \
               self.doi == other.doi and \
               self.publisher == other.publisher and \
               self.journal == other.journal and \
               self.published_date == other.published_date


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
        return self.abstract == other.abstract and \
               self.keywords == other.keywords


@dataclass
class Artical:
    metadata: Metadata
    content: Content

    def __repr__(self):
        return f"Metadata: {self.metadata}\n" \
               f"Content: {self.content}"
