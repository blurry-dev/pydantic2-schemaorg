from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501q(USNonprofitType):
    """Nonprofit501q: Non-profit type referring to Credit Counseling Organizations.

    See: https://schema.org/Nonprofit501q
    Model depth: 6
    """

    type_: str = Field(default="Nonprofit501q", alias="@type", const=True)
