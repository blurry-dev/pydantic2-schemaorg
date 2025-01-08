from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class PlaceOfWorship(CivicStructure):
    """Place of worship, such as a church, synagogue, or mosque.

    See: https://schema.org/PlaceOfWorship
    Model depth: 4
    """

    type_: str = Field(default="PlaceOfWorship", alias="@type", const=True)
