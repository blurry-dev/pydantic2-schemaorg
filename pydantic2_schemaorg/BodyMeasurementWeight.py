from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BodyMeasurementTypeEnumeration import (
    BodyMeasurementTypeEnumeration,
)


class BodyMeasurementWeight(BodyMeasurementTypeEnumeration):
    """Body weight. Used, for example, to measure pantyhose.

    See: https://schema.org/BodyMeasurementWeight
    Model depth: 6
    """

    type_: str = Field(default="BodyMeasurementWeight", alias="@type", const=True)
