from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class BasicIncome(GovernmentBenefitsType):
    """BasicIncome: this is a benefit for basic income.

    See: https://schema.org/BasicIncome
    Model depth: 5
    """

    type_: str = Field(default="BasicIncome", alias="@type", const=True)
