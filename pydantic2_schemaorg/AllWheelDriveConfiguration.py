from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DriveWheelConfigurationValue import (
    DriveWheelConfigurationValue,
)


class AllWheelDriveConfiguration(DriveWheelConfigurationValue):
    """All-wheel Drive is a transmission layout where the engine drives all four wheels.

    See: https://schema.org/AllWheelDriveConfiguration
    Model depth: 6
    """

    type_: str = Field(default="AllWheelDriveConfiguration", alias="@type", const=True)
