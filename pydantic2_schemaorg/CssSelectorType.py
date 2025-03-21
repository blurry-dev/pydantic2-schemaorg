from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Text import Text


class CssSelectorType(Text):
    """Text representing a CSS selector.

    See: https://schema.org/CssSelectorType
    Model depth: 6
    """

    type_: str = Field(default="CssSelectorType", alias="@type", const=True)
