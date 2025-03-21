from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class HousePainter(HomeAndConstructionBusiness):
    """A house painting service.

    See: https://schema.org/HousePainter
    Model depth: 5
    """

    type_: str = Field(default="HousePainter", alias="@type", const=True)
