from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EUEnergyEfficiencyEnumeration import (
    EUEnergyEfficiencyEnumeration,
)


class EUEnergyEfficiencyCategoryE(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class E as defined in EU energy labeling regulations.

    See: https://schema.org/EUEnergyEfficiencyCategoryE
    Model depth: 6
    """

    type_: str = Field(default="EUEnergyEfficiencyCategoryE", alias="@type", const=True)
