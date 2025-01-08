from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic.v1 import AnyUrl
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class Brand(Intangible):
    """A brand is a name used by an organization or business person for labeling a product, product group, or similar.

    See: https://schema.org/Brand
    Model depth: 3
    """

    type_: str = Field(default="Brand", alias="@type", const=True)
    logo: Optional[
        Union[
            List[Union[AnyUrl, "URL", "ImageObject", str]],
            AnyUrl,
            "URL",
            "ImageObject",
            str,
        ]
    ] = Field(
        default=None,
        description="An associated logo.",
    )
    aggregateRating: Optional[
        Union[List[Union["AggregateRating", str]], "AggregateRating", str]
    ] = Field(
        default=None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    slogan: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="A slogan or motto associated with the item.",
    )
    review: Optional[Union[List[Union["Review", str]], "Review", str]] = Field(
        default=None,
        description="A review of the item.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.ImageObject import ImageObject
    from pydantic2_schemaorg.AggregateRating import AggregateRating
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Review import Review
