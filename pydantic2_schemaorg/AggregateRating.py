from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Rating import Rating


class AggregateRating(Rating):
    """The average rating based on multiple ratings or reviews.

    See: https://schema.org/AggregateRating
    Model depth: 4
    """

    type_: str = Field(default="AggregateRating", alias="@type", const=True)
    ratingCount: Optional[
        Union[List[Union[int, "Integer", str]], int, "Integer", str]
    ] = Field(
        default=None,
        description="The count of total number of ratings.",
    )
    reviewCount: Optional[
        Union[List[Union[int, "Integer", str]], int, "Integer", str]
    ] = Field(
        default=None,
        description="The count of total number of reviews.",
    )
    itemReviewed: Optional[Union[List[Union["Thing", str]], "Thing", str]] = Field(
        default=None,
        description="The item that is being reviewed/rated.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Integer import Integer
    from pydantic2_schemaorg.Thing import Thing
