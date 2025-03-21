from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.SteeringPositionValue import SteeringPositionValue


class RightHandDriving(SteeringPositionValue):
    """The steering position is on the right side of the vehicle (viewed from the main direction of driving).

    See: https://schema.org/RightHandDriving
    Model depth: 6
    """

    type_: str = Field(default="RightHandDriving", alias="@type", const=True)
