from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableMeasurementTypeEnumeration import (
    WearableMeasurementTypeEnumeration,
)


class WearableMeasurementChestOrBust(WearableMeasurementTypeEnumeration):
    """Measurement of the chest/bust section, for example of a suit.

    See: https://schema.org/WearableMeasurementChestOrBust
    Model depth: 6
    """

    type_: str = Field(
        default="WearableMeasurementChestOrBust", alias="@type", const=True
    )
