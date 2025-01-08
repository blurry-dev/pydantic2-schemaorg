from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class TierBenefitEnumeration(Enumeration):
    """An enumeration of possible benefits as part of a loyalty (members) program.

    See: https://schema.org/TierBenefitEnumeration
    Model depth: 4
    """

    type_: str = Field(default="TierBenefitEnumeration", alias="@type", const=True)
