from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BodyMeasurementTypeEnumeration import (
    BodyMeasurementTypeEnumeration,
)


class BodyMeasurementBust(BodyMeasurementTypeEnumeration):
    """Maximum girth of bust. Used, for example, to fit women's suits.

    See: https://schema.org/BodyMeasurementBust
    Model depth: 6
    """

    type_: str = Field(default="BodyMeasurementBust", alias="@type", const=True)
