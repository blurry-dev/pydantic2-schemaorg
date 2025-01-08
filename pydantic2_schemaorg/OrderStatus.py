from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.StatusEnumeration import StatusEnumeration


class OrderStatus(StatusEnumeration):
    """Enumerated status values for Order.

    See: https://schema.org/OrderStatus
    Model depth: 5
    """

    type_: str = Field(default="OrderStatus", alias="@type", const=True)
