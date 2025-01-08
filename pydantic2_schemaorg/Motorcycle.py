from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Vehicle import Vehicle


class Motorcycle(Vehicle):
    """A motorcycle or motorbike is a single-track, two-wheeled motor vehicle.

    See: https://schema.org/Motorcycle
    Model depth: 4
    """

    type_: str = Field(default="Motorcycle", alias="@type", const=True)
