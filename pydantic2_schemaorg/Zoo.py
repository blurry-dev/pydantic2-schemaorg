from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class Zoo(CivicStructure):
    """A zoo.

    See: https://schema.org/Zoo
    Model depth: 4
    """

    type_: str = Field(default="Zoo", alias="@type", const=True)
