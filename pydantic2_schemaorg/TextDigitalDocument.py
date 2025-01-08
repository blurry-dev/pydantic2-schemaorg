from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DigitalDocument import DigitalDocument


class TextDigitalDocument(DigitalDocument):
    """A file composed primarily of text.

    See: https://schema.org/TextDigitalDocument
    Model depth: 4
    """

    type_: str = Field(default="TextDigitalDocument", alias="@type", const=True)
