from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.OrderStatus import OrderStatus


class OrderDelivered(OrderStatus):
    """OrderStatus representing successful delivery of an order.

    See: https://schema.org/OrderDelivered
    Model depth: 6
    """

    type_: str = Field(default="OrderDelivered", alias="@type", const=True)
