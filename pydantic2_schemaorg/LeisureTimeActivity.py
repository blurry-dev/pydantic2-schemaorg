from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory


class LeisureTimeActivity(PhysicalActivityCategory):
    """Any physical activity engaged in for recreational purposes. Examples may include ballroom dancing, roller
     skating, canoeing, fishing, etc.

    See: https://schema.org/LeisureTimeActivity
    Model depth: 5
    """

    type_: str = Field(default="LeisureTimeActivity", alias="@type", const=True)
