from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DriveWheelConfigurationValue import (
    DriveWheelConfigurationValue,
)


class RearWheelDriveConfiguration(DriveWheelConfigurationValue):
    """Real-wheel drive is a transmission layout where the engine drives the rear wheels.

    See: https://schema.org/RearWheelDriveConfiguration
    Model depth: 6
    """

    type_: str = Field(default="RearWheelDriveConfiguration", alias="@type", const=True)
