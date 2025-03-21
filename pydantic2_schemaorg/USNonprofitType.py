from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.NonprofitType import NonprofitType


class USNonprofitType(NonprofitType):
    """USNonprofitType: Non-profit organization type originating from the United States.

    See: https://schema.org/USNonprofitType
    Model depth: 5
    """

    type_: str = Field(default="USNonprofitType", alias="@type", const=True)
