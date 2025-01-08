from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class Crematorium(CivicStructure):
    """A crematorium.

    See: https://schema.org/Crematorium
    Model depth: 4
    """

    type_: str = Field(default="Crematorium", alias="@type", const=True)
