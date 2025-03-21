from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DriveWheelConfigurationValue import (
    DriveWheelConfigurationValue,
)


class FrontWheelDriveConfiguration(DriveWheelConfigurationValue):
    """Front-wheel drive is a transmission layout where the engine drives the front wheels.

    See: https://schema.org/FrontWheelDriveConfiguration
    Model depth: 6
    """

    type_: str = Field(
        default="FrontWheelDriveConfiguration", alias="@type", const=True
    )
