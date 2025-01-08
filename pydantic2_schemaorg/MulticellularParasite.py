from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class MulticellularParasite(InfectiousAgentClass):
    """Multicellular parasite that causes an infection.

    See: https://schema.org/MulticellularParasite
    Model depth: 6
    """

    type_: str = Field(default="MulticellularParasite", alias="@type", const=True)
