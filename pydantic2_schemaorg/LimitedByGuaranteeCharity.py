from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.UKNonprofitType import UKNonprofitType


class LimitedByGuaranteeCharity(UKNonprofitType):
    """LimitedByGuaranteeCharity: Non-profit type referring to a charitable company that is limited by guarantee
     (UK).

    See: https://schema.org/LimitedByGuaranteeCharity
    Model depth: 6
    """

    type_: str = Field(default="LimitedByGuaranteeCharity", alias="@type", const=True)
