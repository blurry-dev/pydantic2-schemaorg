from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class BoardingPolicyType(Enumeration):
    """A type of boarding policy used by an airline.

    See: https://schema.org/BoardingPolicyType
    Model depth: 4
    """

    type_: str = Field(default="BoardingPolicyType", alias="@type", const=True)
