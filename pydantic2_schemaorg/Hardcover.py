from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BookFormatType import BookFormatType


class Hardcover(BookFormatType):
    """Book format: Hardcover.

    See: https://schema.org/Hardcover
    Model depth: 5
    """

    type_: str = Field(default="Hardcover", alias="@type", const=True)
