from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EUEnergyEfficiencyEnumeration import (
    EUEnergyEfficiencyEnumeration,
)


class EUEnergyEfficiencyCategoryB(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class B as defined in EU energy labeling regulations.

    See: https://schema.org/EUEnergyEfficiencyCategoryB
    Model depth: 6
    """

    type_: str = Field(default="EUEnergyEfficiencyCategoryB", alias="@type", const=True)
