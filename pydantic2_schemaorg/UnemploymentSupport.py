from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class UnemploymentSupport(GovernmentBenefitsType):
    """UnemploymentSupport: this is a benefit for unemployment support.

    See: https://schema.org/UnemploymentSupport
    Model depth: 5
    """

    type_: str = Field(default="UnemploymentSupport", alias="@type", const=True)
