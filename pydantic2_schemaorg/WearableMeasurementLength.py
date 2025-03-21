from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableMeasurementTypeEnumeration import (
    WearableMeasurementTypeEnumeration,
)


class WearableMeasurementLength(WearableMeasurementTypeEnumeration):
    """Represents the length, for example of a dress.

    See: https://schema.org/WearableMeasurementLength
    Model depth: 6
    """

    type_: str = Field(default="WearableMeasurementLength", alias="@type", const=True)
