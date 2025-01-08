from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableMeasurementTypeEnumeration import (
    WearableMeasurementTypeEnumeration,
)


class WearableMeasurementWidth(WearableMeasurementTypeEnumeration):
    """Measurement of the width, for example of shoes.

    See: https://schema.org/WearableMeasurementWidth
    Model depth: 6
    """

    type_: str = Field(default="WearableMeasurementWidth", alias="@type", const=True)
