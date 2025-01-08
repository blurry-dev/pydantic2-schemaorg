from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BoardingPolicyType import BoardingPolicyType


class ZoneBoardingPolicy(BoardingPolicyType):
    """The airline boards by zones of the plane.

    See: https://schema.org/ZoneBoardingPolicy
    Model depth: 5
    """

    type_: str = Field(default="ZoneBoardingPolicy", alias="@type", const=True)
