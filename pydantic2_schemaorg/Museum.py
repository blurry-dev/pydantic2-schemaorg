from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class Museum(CivicStructure):
    """A museum.

    See: https://schema.org/Museum
    Model depth: 4
    """

    type_: str = Field(default="Museum", alias="@type", const=True)
