from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.QualitativeValue import QualitativeValue


class SteeringPositionValue(QualitativeValue):
    """A value indicating a steering position.

    See: https://schema.org/SteeringPositionValue
    Model depth: 5
    """

    type_: str = Field(default="SteeringPositionValue", alias="@type", const=True)
