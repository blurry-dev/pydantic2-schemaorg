from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class Park(CivicStructure):
    """A park.

    See: https://schema.org/Park
    Model depth: 4
    """

    type_: str = Field(default="Park", alias="@type", const=True)
