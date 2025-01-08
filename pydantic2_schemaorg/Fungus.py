from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Fungus(InfectiousAgentClass):
    """Pathogenic fungus.

    See: https://schema.org/Fungus
    Model depth: 6
    """

    type_: str = Field(default="Fungus", alias="@type", const=True)
