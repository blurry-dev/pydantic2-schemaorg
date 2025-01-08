from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DriveWheelConfigurationValue import (
    DriveWheelConfigurationValue,
)


class FourWheelDriveConfiguration(DriveWheelConfigurationValue):
    """Four-wheel drive is a transmission layout where the engine primarily drives two wheels with a part-time four-wheel
     drive capability.

    See: https://schema.org/FourWheelDriveConfiguration
    Model depth: 6
    """

    type_: str = Field(default="FourWheelDriveConfiguration", alias="@type", const=True)
