from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BodyMeasurementTypeEnumeration import (
    BodyMeasurementTypeEnumeration,
)


class BodyMeasurementHead(BodyMeasurementTypeEnumeration):
    """Maximum girth of head above the ears. Used, for example, to fit hats.

    See: https://schema.org/BodyMeasurementHead
    Model depth: 6
    """

    type_: str = Field(default="BodyMeasurementHead", alias="@type", const=True)
