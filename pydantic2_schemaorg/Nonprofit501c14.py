from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c14(USNonprofitType):
    """Nonprofit501c14: Non-profit type referring to State-Chartered Credit Unions, Mutual Reserve Funds.

    See: https://schema.org/Nonprofit501c14
    Model depth: 6
    """

    type_: str = Field(default="Nonprofit501c14", alias="@type", const=True)
