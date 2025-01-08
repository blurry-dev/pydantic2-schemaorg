from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class BoatTerminal(CivicStructure):
    """A terminal for boats, ships, and other water vessels.

    See: https://schema.org/BoatTerminal
    Model depth: 4
    """

    type_: str = Field(default="BoatTerminal", alias="@type", const=True)
