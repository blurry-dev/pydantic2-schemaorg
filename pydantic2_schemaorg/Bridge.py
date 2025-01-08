from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class Bridge(CivicStructure):
    """A bridge.

    See: https://schema.org/Bridge
    Model depth: 4
    """

    type_: str = Field(default="Bridge", alias="@type", const=True)
