from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.SteeringPositionValue import SteeringPositionValue


class LeftHandDriving(SteeringPositionValue):
    """The steering position is on the left side of the vehicle (viewed from the main direction of driving).

    See: https://schema.org/LeftHandDriving
    Model depth: 6
    """

    type_: str = Field(default="LeftHandDriving", alias="@type", const=True)
