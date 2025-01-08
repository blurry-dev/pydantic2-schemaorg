from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class Sculpture(CreativeWork):
    """A piece of sculpture.

    See: https://schema.org/Sculpture
    Model depth: 3
    """

    type_: str = Field(default="Sculpture", alias="@type", const=True)
