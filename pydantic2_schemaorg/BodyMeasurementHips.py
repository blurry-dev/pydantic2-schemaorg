from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BodyMeasurementTypeEnumeration import (
    BodyMeasurementTypeEnumeration,
)


class BodyMeasurementHips(BodyMeasurementTypeEnumeration):
    """Girth of hips (measured around the buttocks). Used, for example, to fit skirts.

    See: https://schema.org/BodyMeasurementHips
    Model depth: 6
    """

    type_: str = Field(default="BodyMeasurementHips", alias="@type", const=True)
