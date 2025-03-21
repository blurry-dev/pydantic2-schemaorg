from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableMeasurementTypeEnumeration import (
    WearableMeasurementTypeEnumeration,
)


class WearableMeasurementHeight(WearableMeasurementTypeEnumeration):
    """Measurement of the height, for example the heel height of a shoe.

    See: https://schema.org/WearableMeasurementHeight
    Model depth: 6
    """

    type_: str = Field(default="WearableMeasurementHeight", alias="@type", const=True)
