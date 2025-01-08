from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EnergyEfficiencyEnumeration import EnergyEfficiencyEnumeration


class EnergyStarEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    """Used to indicate whether a product is EnergyStar certified.

    See: https://schema.org/EnergyStarEnergyEfficiencyEnumeration
    Model depth: 5
    """

    type_: str = Field(
        default="EnergyStarEnergyEfficiencyEnumeration", alias="@type", const=True
    )
