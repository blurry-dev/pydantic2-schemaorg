from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Article import Article


class ScholarlyArticle(Article):
    """A scholarly article.

    See: https://schema.org/ScholarlyArticle
    Model depth: 4
    """

    type_: str = Field(default="ScholarlyArticle", alias="@type", const=True)
