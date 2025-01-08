from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AdultOrientedEnumeration import AdultOrientedEnumeration


class AlcoholConsideration(AdultOrientedEnumeration):
    """Item contains alcohol or promotes alcohol consumption.

    See: https://schema.org/AlcoholConsideration
    Model depth: 5
    """

    type_: str = Field(default="AlcoholConsideration", alias="@type", const=True)
