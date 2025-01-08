from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.TradeAction import TradeAction


class OrderAction(TradeAction):
    """An agent orders an object/product/service to be delivered/sent.

    See: https://schema.org/OrderAction
    Model depth: 4
    """

    type_: str = Field(default="OrderAction", alias="@type", const=True)
    deliveryMethod: Optional[
        Union[List[Union["DeliveryMethod", str]], "DeliveryMethod", str]
    ] = Field(
        default=None,
        description="A sub property of instrument. The method of delivery.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.DeliveryMethod import DeliveryMethod
