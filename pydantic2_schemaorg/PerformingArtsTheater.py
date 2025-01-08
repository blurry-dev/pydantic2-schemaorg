from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class PerformingArtsTheater(CivicStructure):
    """A theater or other performing art center.

    See: https://schema.org/PerformingArtsTheater
    Model depth: 4
    """

    type_: str = Field(default="PerformingArtsTheater", alias="@type", const=True)
