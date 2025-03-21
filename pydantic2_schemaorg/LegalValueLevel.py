from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class LegalValueLevel(Enumeration):
    """A list of possible levels for the legal validity of a legislation.

    See: https://schema.org/LegalValueLevel
    Model depth: 4
    """

    type_: str = Field(default="LegalValueLevel", alias="@type", const=True)
