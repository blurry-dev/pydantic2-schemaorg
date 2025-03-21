from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BodyMeasurementTypeEnumeration import (
    BodyMeasurementTypeEnumeration,
)


class BodyMeasurementChest(BodyMeasurementTypeEnumeration):
    """Maximum girth of chest. Used, for example, to fit men's suits.

    See: https://schema.org/BodyMeasurementChest
    Model depth: 6
    """

    type_: str = Field(default="BodyMeasurementChest", alias="@type", const=True)
