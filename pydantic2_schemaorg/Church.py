from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PlaceOfWorship import PlaceOfWorship


class Church(PlaceOfWorship):
    """A church.

    See: https://schema.org/Church
    Model depth: 5
    """

    type_: str = Field(default="Church", alias="@type", const=True)
