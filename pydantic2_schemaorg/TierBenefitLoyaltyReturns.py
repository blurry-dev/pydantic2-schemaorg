from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.TierBenefitEnumeration import TierBenefitEnumeration


class TierBenefitLoyaltyReturns(TierBenefitEnumeration):
    """Benefit of the tier is members-only returns, for example free unlimited returns.

    See: https://schema.org/TierBenefitLoyaltyReturns
    Model depth: 5
    """

    type_: str = Field(default="TierBenefitLoyaltyReturns", alias="@type", const=True)
