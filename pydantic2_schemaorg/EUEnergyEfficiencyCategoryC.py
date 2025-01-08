from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EUEnergyEfficiencyEnumeration import (
    EUEnergyEfficiencyEnumeration,
)


class EUEnergyEfficiencyCategoryC(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class C as defined in EU energy labeling regulations.

    See: https://schema.org/EUEnergyEfficiencyCategoryC
    Model depth: 6
    """

    type_: str = Field(default="EUEnergyEfficiencyCategoryC", alias="@type", const=True)
