from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.SportsActivityLocation import SportsActivityLocation
from pydantic2_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class HealthClub(SportsActivityLocation, HealthAndBeautyBusiness):
    """A health club.

    See: https://schema.org/HealthClub
    Model depth: 5
    """

    type_: str = Field(default="HealthClub", alias="@type", const=True)
