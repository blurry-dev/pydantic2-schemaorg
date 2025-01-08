from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class PawnShop(Store):
    """A shop that will buy, or lend money against the security of, personal possessions.

    See: https://schema.org/PawnShop
    Model depth: 5
    """

    type_: str = Field(default="PawnShop", alias="@type", const=True)
