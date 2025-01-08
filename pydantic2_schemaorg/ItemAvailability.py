from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class ItemAvailability(Enumeration):
    """A list of possible product availability options.

    See: https://schema.org/ItemAvailability
    Model depth: 4
    """

    type_: str = Field(default="ItemAvailability", alias="@type", const=True)
