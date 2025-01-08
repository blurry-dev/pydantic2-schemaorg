from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.HowToItem import HowToItem


class HowToSupply(HowToItem):
    """A supply consumed when performing the instructions for how to achieve a result.

    See: https://schema.org/HowToSupply
    Model depth: 5
    """

    type_: str = Field(default="HowToSupply", alias="@type", const=True)
    estimatedCost: Optional[
        Union[List[Union[str, "Text", "MonetaryAmount"]], str, "Text", "MonetaryAmount"]
    ] = Field(
        default=None,
        description="The estimated cost of the supply or supplies consumed when performing instructions.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.MonetaryAmount import MonetaryAmount
