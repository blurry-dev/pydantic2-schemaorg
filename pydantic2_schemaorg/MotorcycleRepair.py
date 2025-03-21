from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class MotorcycleRepair(AutomotiveBusiness):
    """A motorcycle repair shop.

    See: https://schema.org/MotorcycleRepair
    Model depth: 5
    """

    type_: str = Field(default="MotorcycleRepair", alias="@type", const=True)
