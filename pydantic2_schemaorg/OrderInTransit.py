from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.OrderStatus import OrderStatus


class OrderInTransit(OrderStatus):
    """OrderStatus representing that an order is in transit.

    See: https://schema.org/OrderInTransit
    Model depth: 6
    """

    type_: str = Field(default="OrderInTransit", alias="@type", const=True)
