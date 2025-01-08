from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class MeasurementMethodEnum(Enumeration):
    """Enumeration(s) for use with [[measurementMethod]].

    See: https://schema.org/MeasurementMethodEnum
    Model depth: 4
    """

    type_: str = Field(default="MeasurementMethodEnum", alias="@type", const=True)
