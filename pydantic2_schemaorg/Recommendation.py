from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic.v1 import AnyUrl
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Review import Review


class Recommendation(Review):
    """[[Recommendation]] is a type of [[Review]] that suggests or proposes something as the best option or best
     course of action. Recommendations may be for products or services, or other concrete things, as in the case
     of a ranked list or product guide. A [[Guide]] may list multiple recommendations for different categories.
     For example, in a [[Guide]] about which TVs to buy, the author may have several [[Recommendation]]s.

    See: https://schema.org/Recommendation
    Model depth: 4
    """

    type_: str = Field(default="Recommendation", alias="@type", const=True)
    category: Optional[
        Union[
            List[
                Union[
                    AnyUrl,
                    "URL",
                    str,
                    "Text",
                    "PhysicalActivityCategory",
                    "CategoryCode",
                    "Thing",
                ]
            ],
            AnyUrl,
            "URL",
            str,
            "Text",
            "PhysicalActivityCategory",
            "CategoryCode",
            "Thing",
        ]
    ] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
    from pydantic2_schemaorg.CategoryCode import CategoryCode
    from pydantic2_schemaorg.Thing import Thing
