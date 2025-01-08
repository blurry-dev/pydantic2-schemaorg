from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic.v1 import StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.ListItem import ListItem


class HowToItem(ListItem):
    """An item used as either a tool or supply when performing the instructions for how to achieve a result.

    See: https://schema.org/HowToItem
    Model depth: 4
    """

    type_: str = Field(default="HowToItem", alias="@type", const=True)
    requiredQuantity: Optional[
        Union[
            List[
                Union[
                    StrictInt, StrictFloat, "Number", str, "Text", "QuantitativeValue"
                ]
            ],
            StrictInt,
            StrictFloat,
            "Number",
            str,
            "Text",
            "QuantitativeValue",
        ]
    ] = Field(
        default=None,
        description="The required quantity of the item(s).",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.QuantitativeValue import QuantitativeValue
