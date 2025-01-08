from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EnergyStarEnergyEfficiencyEnumeration import (
    EnergyStarEnergyEfficiencyEnumeration,
)


class EnergyStarCertified(EnergyStarEnergyEfficiencyEnumeration):
    """Represents EnergyStar certification.

    See: https://schema.org/EnergyStarCertified
    Model depth: 6
    """

    type_: str = Field(default="EnergyStarCertified", alias="@type", const=True)
