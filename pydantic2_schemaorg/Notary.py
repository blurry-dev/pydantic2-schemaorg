from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LegalService import LegalService


class Notary(LegalService):
    """A notary.

    See: https://schema.org/Notary
    Model depth: 5
    """

    type_: str = Field(default="Notary", alias="@type", const=True)
