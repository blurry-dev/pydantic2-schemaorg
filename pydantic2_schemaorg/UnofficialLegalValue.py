from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LegalValueLevel import LegalValueLevel


class UnofficialLegalValue(LegalValueLevel):
    """Indicates that a document has no particular or special standing (e.g. a republication of a law by a private
     publisher).

    See: https://schema.org/UnofficialLegalValue
    Model depth: 5
    """

    type_: str = Field(default="UnofficialLegalValue", alias="@type", const=True)
