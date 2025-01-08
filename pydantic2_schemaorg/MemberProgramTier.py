from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import StrictInt, StrictFloat


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class MemberProgramTier(Intangible):
    """A MemberProgramTier specifies a tier under a loyalty (member) program, for example \"gold\".

    See: https://schema.org/MemberProgramTier
    Model depth: 3
    """

    type_: str = Field(default="MemberProgramTier", alias="@type", const=True)
    hasTierBenefit: Optional[
        Union[List[Union["TierBenefitEnumeration", str]], "TierBenefitEnumeration", str]
    ] = Field(
        default=None,
        description="A member benefit for a particular tier of a loyalty program.",
    )
    membershipPointsEarned: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", "QuantitativeValue", str]],
            StrictInt,
            StrictFloat,
            "Number",
            "QuantitativeValue",
            str,
        ]
    ] = Field(
        default=None,
        description="The number of membership points earned by the member. If necessary, the unitText can be used to express the units the points are issued in. (E.g. stars, miles, etc.)",
    )
    isTierOf: Optional[
        Union[List[Union["MemberProgram", str]], "MemberProgram", str]
    ] = Field(
        default=None,
        description="The member program this tier is a part of.",
    )
    hasTierRequirement: Optional[
        Union[
            List[
                Union[
                    str,
                    "Text",
                    "MonetaryAmount",
                    "CreditCard",
                    "UnitPriceSpecification",
                ]
            ],
            str,
            "Text",
            "MonetaryAmount",
            "CreditCard",
            "UnitPriceSpecification",
        ]
    ] = Field(
        default=None,
        description="A requirement for a user to join a membership tier, for example: a CreditCard if the tier requires sign up for a credit card, A UnitPriceSpecification if the user is required to pay a (periodic) fee, or a MonetaryAmount if the user needs to spend a minimum amount to join the tier. If a tier is free to join then this property does not need to be specified.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.TierBenefitEnumeration import TierBenefitEnumeration
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic2_schemaorg.MemberProgram import MemberProgram
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic2_schemaorg.CreditCard import CreditCard
    from pydantic2_schemaorg.UnitPriceSpecification import UnitPriceSpecification
