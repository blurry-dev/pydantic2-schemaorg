from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c21(USNonprofitType):
    """Nonprofit501c21: Non-profit type referring to Black Lung Benefit Trusts.

    See: https://schema.org/Nonprofit501c21
    Model depth: 6
    """

    type_: str = Field(default="Nonprofit501c21", alias="@type", const=True)
