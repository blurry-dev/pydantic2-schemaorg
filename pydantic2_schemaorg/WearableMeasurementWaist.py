from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableMeasurementTypeEnumeration import (
    WearableMeasurementTypeEnumeration,
)


class WearableMeasurementWaist(WearableMeasurementTypeEnumeration):
    """Measurement of the waist section, for example of pants.

    See: https://schema.org/WearableMeasurementWaist
    Model depth: 6
    """

    type_: str = Field(default="WearableMeasurementWaist", alias="@type", const=True)
