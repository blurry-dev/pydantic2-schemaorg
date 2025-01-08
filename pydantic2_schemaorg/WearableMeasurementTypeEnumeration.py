from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MeasurementTypeEnumeration import MeasurementTypeEnumeration


class WearableMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """Enumerates common types of measurement for wearables products.

    See: https://schema.org/WearableMeasurementTypeEnumeration
    Model depth: 5
    """

    type_: str = Field(
        default="WearableMeasurementTypeEnumeration", alias="@type", const=True
    )
