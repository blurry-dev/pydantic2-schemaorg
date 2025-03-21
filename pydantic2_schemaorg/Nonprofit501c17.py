from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c17(USNonprofitType):
    """Nonprofit501c17: Non-profit type referring to Supplemental Unemployment Benefit Trusts.

    See: https://schema.org/Nonprofit501c17
    Model depth: 6
    """

    type_: str = Field(default="Nonprofit501c17", alias="@type", const=True)
