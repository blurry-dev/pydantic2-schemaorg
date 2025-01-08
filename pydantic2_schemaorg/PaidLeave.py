from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class PaidLeave(GovernmentBenefitsType):
    """PaidLeave: this is a benefit for paid leave.

    See: https://schema.org/PaidLeave
    Model depth: 5
    """

    type_: str = Field(default="PaidLeave", alias="@type", const=True)
