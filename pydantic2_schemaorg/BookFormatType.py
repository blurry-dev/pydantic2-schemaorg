from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class BookFormatType(Enumeration):
    """The publication format of the book.

    See: https://schema.org/BookFormatType
    Model depth: 4
    """

    type_: str = Field(default="BookFormatType", alias="@type", const=True)
