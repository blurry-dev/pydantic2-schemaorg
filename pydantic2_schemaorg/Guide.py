from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class Guide(CreativeWork):
    """[[Guide]] is a page or article that recommends specific products or services, or aspects of a thing for a user
     to consider. A [[Guide]] may represent a Buying Guide and detail aspects of products or services for a user
     to consider. A [[Guide]] may represent a Product Guide and recommend specific products or services. A [[Guide]]
     may represent a Ranked List and recommend specific products or services with ranking.

    See: https://schema.org/Guide
    Model depth: 3
    """

    type_: str = Field(default="Guide", alias="@type", const=True)
    reviewAspect: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="This Review or Rating is relevant to this part or facet of the itemReviewed.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
