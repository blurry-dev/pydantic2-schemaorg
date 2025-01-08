from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class HairSalon(HealthAndBeautyBusiness):
    """A hair salon.

    See: https://schema.org/HairSalon
    Model depth: 5
    """

    type_: str = Field(default="HairSalon", alias="@type", const=True)
