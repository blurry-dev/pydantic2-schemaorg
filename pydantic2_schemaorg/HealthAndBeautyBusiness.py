from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class HealthAndBeautyBusiness(LocalBusiness):
    """Health and beauty.

    See: https://schema.org/HealthAndBeautyBusiness
    Model depth: 4
    """

    type_: str = Field(default="HealthAndBeautyBusiness", alias="@type", const=True)
