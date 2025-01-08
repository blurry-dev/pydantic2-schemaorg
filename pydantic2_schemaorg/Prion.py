from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Prion(InfectiousAgentClass):
    """A prion is an infectious agent composed of protein in a misfolded form.

    See: https://schema.org/Prion
    Model depth: 6
    """

    type_: str = Field(default="Prion", alias="@type", const=True)
