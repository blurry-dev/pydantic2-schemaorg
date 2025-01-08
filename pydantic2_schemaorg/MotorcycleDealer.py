from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class MotorcycleDealer(AutomotiveBusiness):
    """A motorcycle dealer.

    See: https://schema.org/MotorcycleDealer
    Model depth: 5
    """

    type_: str = Field(default="MotorcycleDealer", alias="@type", const=True)
