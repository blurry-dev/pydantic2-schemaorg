from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class Photograph(CreativeWork):
    """A photograph.

    See: https://schema.org/Photograph
    Model depth: 3
    """

    type_: str = Field(default="Photograph", alias="@type", const=True)
