from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class BusinessSupport(GovernmentBenefitsType):
    """BusinessSupport: this is a benefit for supporting businesses.

    See: https://schema.org/BusinessSupport
    Model depth: 5
    """

    type_: str = Field(default="BusinessSupport", alias="@type", const=True)
