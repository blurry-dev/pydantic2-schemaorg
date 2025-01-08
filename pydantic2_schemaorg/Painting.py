from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class Painting(CreativeWork):
    """A painting.

    See: https://schema.org/Painting
    Model depth: 3
    """

    type_: str = Field(default="Painting", alias="@type", const=True)
