from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class Cemetery(CivicStructure):
    """A graveyard.

    See: https://schema.org/Cemetery
    Model depth: 4
    """

    type_: str = Field(default="Cemetery", alias="@type", const=True)
