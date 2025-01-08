from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.NonprofitType import NonprofitType


class NLNonprofitType(NonprofitType):
    """NLNonprofitType: Non-profit organization type originating from the Netherlands.

    See: https://schema.org/NLNonprofitType
    Model depth: 5
    """

    type_: str = Field(default="NLNonprofitType", alias="@type", const=True)
