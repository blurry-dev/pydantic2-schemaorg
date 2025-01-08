from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class TattooParlor(HealthAndBeautyBusiness):
    """A tattoo parlor.

    See: https://schema.org/TattooParlor
    Model depth: 5
    """

    type_: str = Field(default="TattooParlor", alias="@type", const=True)
