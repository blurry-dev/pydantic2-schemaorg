from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class GovernmentBenefitsType(Enumeration):
    """GovernmentBenefitsType enumerates several kinds of government benefits to support the COVID-19 situation.
     Note that this structure may not capture all benefits offered.

    See: https://schema.org/GovernmentBenefitsType
    Model depth: 4
    """

    type_: str = Field(default="GovernmentBenefitsType", alias="@type", const=True)
