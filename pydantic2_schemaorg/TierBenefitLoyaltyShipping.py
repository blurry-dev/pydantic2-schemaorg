from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.TierBenefitEnumeration import TierBenefitEnumeration


class TierBenefitLoyaltyShipping(TierBenefitEnumeration):
    """Benefit of the tier is a members-only shipping price or speed (for example free shipping or 1-day shipping).

    See: https://schema.org/TierBenefitLoyaltyShipping
    Model depth: 5
    """

    type_: str = Field(default="TierBenefitLoyaltyShipping", alias="@type", const=True)
