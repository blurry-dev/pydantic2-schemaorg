from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AggregateRating import AggregateRating


class EmployerAggregateRating(AggregateRating):
    """An aggregate rating of an Organization related to its role as an employer.

    See: https://schema.org/EmployerAggregateRating
    Model depth: 5
    """

    type_: str = Field(default="EmployerAggregateRating", alias="@type", const=True)
