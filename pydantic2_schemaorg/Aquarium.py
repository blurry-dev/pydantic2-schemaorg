from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class Aquarium(CivicStructure):
    """Aquarium.

    See: https://schema.org/Aquarium
    Model depth: 4
    """

    type_: str = Field(default="Aquarium", alias="@type", const=True)
