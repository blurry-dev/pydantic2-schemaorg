from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class OneTimePayments(GovernmentBenefitsType):
    """OneTimePayments: this is a benefit for one-time payments for individuals.

    See: https://schema.org/OneTimePayments
    Model depth: 5
    """

    type_: str = Field(default="OneTimePayments", alias="@type", const=True)
