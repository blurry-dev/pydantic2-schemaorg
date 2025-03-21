from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.OrderStatus import OrderStatus


class OrderPickupAvailable(OrderStatus):
    """OrderStatus representing availability of an order for pickup.

    See: https://schema.org/OrderPickupAvailable
    Model depth: 6
    """

    type_: str = Field(default="OrderPickupAvailable", alias="@type", const=True)
