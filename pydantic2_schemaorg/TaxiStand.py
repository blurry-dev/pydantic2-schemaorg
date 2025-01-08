from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class TaxiStand(CivicStructure):
    """A taxi stand.

    See: https://schema.org/TaxiStand
    Model depth: 4
    """

    type_: str = Field(default="TaxiStand", alias="@type", const=True)
