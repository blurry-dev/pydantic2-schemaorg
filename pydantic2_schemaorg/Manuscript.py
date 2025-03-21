from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class Manuscript(CreativeWork):
    """A book, document, or piece of music written by hand rather than typed or printed.

    See: https://schema.org/Manuscript
    Model depth: 3
    """

    type_: str = Field(default="Manuscript", alias="@type", const=True)
