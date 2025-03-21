from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableMeasurementTypeEnumeration import (
    WearableMeasurementTypeEnumeration,
)


class WearableMeasurementSleeve(WearableMeasurementTypeEnumeration):
    """Measurement of the sleeve length, for example of a shirt.

    See: https://schema.org/WearableMeasurementSleeve
    Model depth: 6
    """

    type_: str = Field(default="WearableMeasurementSleeve", alias="@type", const=True)
