from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501n(USNonprofitType):
    """Nonprofit501n: Non-profit type referring to Charitable Risk Pools.

    See: https://schema.org/Nonprofit501n
    Model depth: 6
    """

    type_: str = Field(default="Nonprofit501n", alias="@type", const=True)
