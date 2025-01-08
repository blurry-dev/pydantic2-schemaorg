from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c26(USNonprofitType):
    """Nonprofit501c26: Non-profit type referring to State-Sponsored Organizations Providing Health Coverage
     for High-Risk Individuals.

    See: https://schema.org/Nonprofit501c26
    Model depth: 6
    """

    type_: str = Field(default="Nonprofit501c26", alias="@type", const=True)
