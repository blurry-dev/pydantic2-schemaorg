from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.OrderStatus import OrderStatus


class OrderProcessing(OrderStatus):
    """OrderStatus representing that an order is being processed.

    See: https://schema.org/OrderProcessing
    Model depth: 6
    """

    type_: str = Field(default="OrderProcessing", alias="@type", const=True)
