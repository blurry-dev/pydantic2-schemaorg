from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Service import Service


class Taxi(Service):
    """A taxi.

    See: https://schema.org/Taxi
    Model depth: 4
    """

    type_: str = Field(default="Taxi", alias="@type", const=True)
