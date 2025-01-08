from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class BeautySalon(HealthAndBeautyBusiness):
    """Beauty salon.

    See: https://schema.org/BeautySalon
    Model depth: 5
    """

    type_: str = Field(default="BeautySalon", alias="@type", const=True)
