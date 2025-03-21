from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.UKNonprofitType import UKNonprofitType


class UKTrust(UKNonprofitType):
    """UKTrust: Non-profit type referring to a UK trust.

    See: https://schema.org/UKTrust
    Model depth: 6
    """

    type_: str = Field(default="UKTrust", alias="@type", const=True)
