from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BookFormatType import BookFormatType


class EBook(BookFormatType):
    """Book format: Ebook.

    See: https://schema.org/EBook
    Model depth: 5
    """

    type_: str = Field(default="EBook", alias="@type", const=True)
