from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BodyMeasurementTypeEnumeration import (
    BodyMeasurementTypeEnumeration,
)


class BodyMeasurementHeight(BodyMeasurementTypeEnumeration):
    """Body height (measured between crown of head and soles of feet). Used, for example, to fit jackets.

    See: https://schema.org/BodyMeasurementHeight
    Model depth: 6
    """

    type_: str = Field(default="BodyMeasurementHeight", alias="@type", const=True)
