from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class Playground(CivicStructure):
    """A playground.

    See: https://schema.org/Playground
    Model depth: 4
    """

    type_: str = Field(default="Playground", alias="@type", const=True)
