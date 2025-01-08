from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CriticReview import CriticReview
from pydantic2_schemaorg.NewsArticle import NewsArticle


class ReviewNewsArticle(CriticReview, NewsArticle):
    """A [[NewsArticle]] and [[CriticReview]] providing a professional critic's assessment of a service, product,
     performance, or artistic or literary work.

    See: https://schema.org/ReviewNewsArticle
    Model depth: 5
    """

    type_: str = Field(default="ReviewNewsArticle", alias="@type", const=True)
