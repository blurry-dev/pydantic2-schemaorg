from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BookFormatType import BookFormatType


class Paperback(BookFormatType):
    """Book format: Paperback.

    See: https://schema.org/Paperback
    Model depth: 5
    """

    type_: str = Field(default="Paperback", alias="@type", const=True)
