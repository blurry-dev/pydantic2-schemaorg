from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DeliveryMethod import DeliveryMethod


class LockerDelivery(DeliveryMethod):
    """A DeliveryMethod in which an item is made available via locker.

    See: https://schema.org/LockerDelivery
    Model depth: 5
    """

    type_: str = Field(default="LockerDelivery", alias="@type", const=True)
