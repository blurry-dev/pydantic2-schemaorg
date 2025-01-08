from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EUEnergyEfficiencyEnumeration import (
    EUEnergyEfficiencyEnumeration,
)


class EUEnergyEfficiencyCategoryF(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class F as defined in EU energy labeling regulations.

    See: https://schema.org/EUEnergyEfficiencyCategoryF
    Model depth: 6
    """

    type_: str = Field(default="EUEnergyEfficiencyCategoryF", alias="@type", const=True)
