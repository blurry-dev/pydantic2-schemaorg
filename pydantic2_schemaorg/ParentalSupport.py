from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class ParentalSupport(GovernmentBenefitsType):
    """ParentalSupport: this is a benefit for parental support.

    See: https://schema.org/ParentalSupport
    Model depth: 5
    """

    type_: str = Field(default="ParentalSupport", alias="@type", const=True)
