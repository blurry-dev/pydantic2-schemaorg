from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BodyMeasurementTypeEnumeration import (
    BodyMeasurementTypeEnumeration,
)


class BodyMeasurementInsideLeg(BodyMeasurementTypeEnumeration):
    """Inside leg (measured between crotch and soles of feet). Used, for example, to fit pants.

    See: https://schema.org/BodyMeasurementInsideLeg
    Model depth: 6
    """

    type_: str = Field(default="BodyMeasurementInsideLeg", alias="@type", const=True)
