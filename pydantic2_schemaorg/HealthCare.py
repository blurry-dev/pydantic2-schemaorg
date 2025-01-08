from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class HealthCare(GovernmentBenefitsType):
    """HealthCare: this is a benefit for health care.

    See: https://schema.org/HealthCare
    Model depth: 5
    """

    type_: str = Field(default="HealthCare", alias="@type", const=True)
