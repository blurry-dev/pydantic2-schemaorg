from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoBodyShop(AutomotiveBusiness):
    """Auto body shop.

    See: https://schema.org/AutoBodyShop
    Model depth: 5
    """

    type_: str = Field(default="AutoBodyShop", alias="@type", const=True)
