from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EUEnergyEfficiencyEnumeration import (
    EUEnergyEfficiencyEnumeration,
)


class EUEnergyEfficiencyCategoryA(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class A as defined in EU energy labeling regulations.

    See: https://schema.org/EUEnergyEfficiencyCategoryA
    Model depth: 6
    """

    type_: str = Field(default="EUEnergyEfficiencyCategoryA", alias="@type", const=True)
