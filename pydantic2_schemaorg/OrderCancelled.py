from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.OrderStatus import OrderStatus


class OrderCancelled(OrderStatus):
    """OrderStatus representing cancellation of an order.

    See: https://schema.org/OrderCancelled
    Model depth: 6
    """

    type_: str = Field(default="OrderCancelled", alias="@type", const=True)
