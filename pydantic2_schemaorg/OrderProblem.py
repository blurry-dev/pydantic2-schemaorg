from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.OrderStatus import OrderStatus


class OrderProblem(OrderStatus):
    """OrderStatus representing that there is a problem with the order.

    See: https://schema.org/OrderProblem
    Model depth: 6
    """

    type_: str = Field(default="OrderProblem", alias="@type", const=True)
