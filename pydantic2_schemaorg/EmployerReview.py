from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Review import Review


class EmployerReview(Review):
    """An [[EmployerReview]] is a review of an [[Organization]] regarding its role as an employer, written by a current
     or former employee of that organization.

    See: https://schema.org/EmployerReview
    Model depth: 4
    """

    type_: str = Field(default="EmployerReview", alias="@type", const=True)
