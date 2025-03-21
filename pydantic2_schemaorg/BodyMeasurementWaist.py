from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BodyMeasurementTypeEnumeration import (
    BodyMeasurementTypeEnumeration,
)


class BodyMeasurementWaist(BodyMeasurementTypeEnumeration):
    """Girth of natural waistline (between hip bones and lower ribs). Used, for example, to fit pants.

    See: https://schema.org/BodyMeasurementWaist
    Model depth: 6
    """

    type_: str = Field(default="BodyMeasurementWaist", alias="@type", const=True)
