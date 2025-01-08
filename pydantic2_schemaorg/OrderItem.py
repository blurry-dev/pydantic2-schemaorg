from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import StrictInt, StrictFloat


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class OrderItem(Intangible):
    """An order item is a line of an order. It includes the quantity and shipping details of a bought offer.

    See: https://schema.org/OrderItem
    Model depth: 3
    """

    type_: str = Field(default="OrderItem", alias="@type", const=True)
    orderItemStatus: Optional[
        Union[List[Union["OrderStatus", str]], "OrderStatus", str]
    ] = Field(
        default=None,
        description="The current status of the order item.",
    )
    orderDelivery: Optional[
        Union[List[Union["ParcelDelivery", str]], "ParcelDelivery", str]
    ] = Field(
        default=None,
        description="The delivery of the parcel related to this order or order item.",
    )
    orderItemNumber: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The identifier of the order item.",
    )
    orderedItem: Optional[
        Union[
            List[Union["OrderItem", "Service", "Product", str]],
            "OrderItem",
            "Service",
            "Product",
            str,
        ]
    ] = Field(
        default=None,
        description="The item ordered.",
    )
    orderQuantity: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", str]],
            StrictInt,
            StrictFloat,
            "Number",
            str,
        ]
    ] = Field(
        default=None,
        description="The number of the item ordered. If the property is not set, assume the quantity is one.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.OrderStatus import OrderStatus
    from pydantic2_schemaorg.ParcelDelivery import ParcelDelivery
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Service import Service
    from pydantic2_schemaorg.Product import Product
    from pydantic2_schemaorg.Number import Number
