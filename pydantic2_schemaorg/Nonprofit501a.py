from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501a(USNonprofitType):
    """Nonprofit501a: Non-profit type referring to Farmers’ Cooperative Associations.

    See: https://schema.org/Nonprofit501a
    Model depth: 6
    """

    type_: str = Field(default="Nonprofit501a", alias="@type", const=True)
