from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c9(USNonprofitType):
    """Nonprofit501c9: Non-profit type referring to Voluntary Employee Beneficiary Associations.

    See: https://schema.org/Nonprofit501c9
    Model depth: 6
    """

    type_: str = Field(default="Nonprofit501c9", alias="@type", const=True)
