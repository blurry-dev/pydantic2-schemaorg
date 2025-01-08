from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501f(USNonprofitType):
    """Nonprofit501f: Non-profit type referring to Cooperative Service Organizations.

    See: https://schema.org/Nonprofit501f
    Model depth: 6
    """

    type_: str = Field(default="Nonprofit501f", alias="@type", const=True)
