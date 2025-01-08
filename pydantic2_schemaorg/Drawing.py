from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class Drawing(CreativeWork):
    """A picture or diagram made with a pencil, pen, or crayon rather than paint.

    See: https://schema.org/Drawing
    Model depth: 3
    """

    type_: str = Field(default="Drawing", alias="@type", const=True)
