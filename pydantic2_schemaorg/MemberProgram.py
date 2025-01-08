from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class MemberProgram(Intangible):
    """A MemberProgram defines a loyalty (or membership) program that provides its members with certain benefits,
     for example better pricing, free shipping or returns, or the ability to earn loyalty points. Member programs
     may have multiple tiers, for example silver and gold members, each with different benefits.

    See: https://schema.org/MemberProgram
    Model depth: 3
    """

    type_: str = Field(default="MemberProgram", alias="@type", const=True)
    hasTiers: Optional[
        Union[List[Union["MemberProgramTier", str]], "MemberProgramTier", str]
    ] = Field(
        default=None,
        description="The tiers of a member program.",
    )
    hostingOrganization: Optional[
        Union[List[Union["Organization", str]], "Organization", str]
    ] = Field(
        default=None,
        description="The Organization (airline, travelers' club, retailer, etc.) the membership is made with or which offers the MemberProgram.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.MemberProgramTier import MemberProgramTier
    from pydantic2_schemaorg.Organization import Organization
