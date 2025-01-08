from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Virus(InfectiousAgentClass):
    """Pathogenic virus that causes viral infection.

    See: https://schema.org/Virus
    Model depth: 6
    """

    type_: str = Field(default="Virus", alias="@type", const=True)
