from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class HobbyShop(Store):
    """A store that sells materials useful or necessary for various hobbies.

    See: https://schema.org/HobbyShop
    Model depth: 5
    """

    type_: str = Field(default="HobbyShop", alias="@type", const=True)
