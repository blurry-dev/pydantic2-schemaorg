from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MeasurementMethodEnum import MeasurementMethodEnum


class ExampleMeasurementMethodEnum(MeasurementMethodEnum):
    """An example [[MeasurementMethodEnum]] (to remove when real enums are added).

    See: https://schema.org/ExampleMeasurementMethodEnum
    Model depth: 5
    """

    type_: str = Field(
        default="ExampleMeasurementMethodEnum", alias="@type", const=True
    )
