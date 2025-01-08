from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c19(USNonprofitType):
    """Nonprofit501c19: Non-profit type referring to Post or Organization of Past or Present Members of the Armed
     Forces.

    See: https://schema.org/Nonprofit501c19
    Model depth: 6
    """

    type_: str = Field(default="Nonprofit501c19", alias="@type", const=True)
