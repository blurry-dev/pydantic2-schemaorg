from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableMeasurementTypeEnumeration import (
    WearableMeasurementTypeEnumeration,
)


class WearableMeasurementHips(WearableMeasurementTypeEnumeration):
    """Measurement of the hip section, for example of a skirt.

    See: https://schema.org/WearableMeasurementHips
    Model depth: 6
    """

    type_: str = Field(default="WearableMeasurementHips", alias="@type", const=True)
