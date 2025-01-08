from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class NailSalon(HealthAndBeautyBusiness):
    """A nail salon.

    See: https://schema.org/NailSalon
    Model depth: 5
    """

    type_: str = Field(default="NailSalon", alias="@type", const=True)
