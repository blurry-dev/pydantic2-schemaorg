from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.NLNonprofitType import NLNonprofitType


class NonprofitSBBI(NLNonprofitType):
    """NonprofitSBBI: Non-profit type referring to a Social Interest Promoting Institution (NL).

    See: https://schema.org/NonprofitSBBI
    Model depth: 6
    """

    type_: str = Field(default="NonprofitSBBI", alias="@type", const=True)
