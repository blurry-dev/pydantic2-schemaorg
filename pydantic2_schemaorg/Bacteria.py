from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Bacteria(InfectiousAgentClass):
    """Pathogenic bacteria that cause bacterial infection.

    See: https://schema.org/Bacteria
    Model depth: 6
    """

    type_: str = Field(default="Bacteria", alias="@type", const=True)
