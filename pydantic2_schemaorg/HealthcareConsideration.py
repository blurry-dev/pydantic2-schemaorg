from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AdultOrientedEnumeration import AdultOrientedEnumeration


class HealthcareConsideration(AdultOrientedEnumeration):
    """Item is a pharmaceutical (e.g., a prescription or OTC drug) or a restricted medical device.

    See: https://schema.org/HealthcareConsideration
    Model depth: 5
    """

    type_: str = Field(default="HealthcareConsideration", alias="@type", const=True)
