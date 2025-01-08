from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class DisabilitySupport(GovernmentBenefitsType):
    """DisabilitySupport: this is a benefit for disability support.

    See: https://schema.org/DisabilitySupport
    Model depth: 5
    """

    type_: str = Field(default="DisabilitySupport", alias="@type", const=True)
