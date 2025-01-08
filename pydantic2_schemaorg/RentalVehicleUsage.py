from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CarUsageType import CarUsageType


class RentalVehicleUsage(CarUsageType):
    """Indicates the usage of the vehicle as a rental car.

    See: https://schema.org/RentalVehicleUsage
    Model depth: 5
    """

    type_: str = Field(default="RentalVehicleUsage", alias="@type", const=True)
