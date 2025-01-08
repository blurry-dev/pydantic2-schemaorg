from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Protozoa(InfectiousAgentClass):
    """Single-celled organism that causes an infection.

    See: https://schema.org/Protozoa
    Model depth: 6
    """

    type_: str = Field(default="Protozoa", alias="@type", const=True)
