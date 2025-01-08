from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.OrderStatus import OrderStatus


class OrderReturned(OrderStatus):
    """OrderStatus representing that an order has been returned.

    See: https://schema.org/OrderReturned
    Model depth: 6
    """

    type_: str = Field(default="OrderReturned", alias="@type", const=True)
