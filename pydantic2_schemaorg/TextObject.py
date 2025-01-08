from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MediaObject import MediaObject


class TextObject(MediaObject):
    """A text file. The text can be unformatted or contain markup, html, etc.

    See: https://schema.org/TextObject
    Model depth: 4
    """

    type_: str = Field(default="TextObject", alias="@type", const=True)
