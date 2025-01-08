from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import StrictBool


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class Book(CreativeWork):
    """A book.

    See: https://schema.org/Book
    Model depth: 3
    """

    type_: str = Field(default="Book", alias="@type", const=True)
    numberOfPages: Optional[
        Union[List[Union[int, "Integer", str]], int, "Integer", str]
    ] = Field(
        default=None,
        description="The number of pages in the book.",
    )
    bookEdition: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The edition of the book.",
    )
    abridged: Optional[
        Union[List[Union[StrictBool, "Boolean", str]], StrictBool, "Boolean", str]
    ] = Field(
        default=None,
        description="Indicates whether the book is an abridged edition.",
    )
    bookFormat: Optional[
        Union[List[Union["BookFormatType", str]], "BookFormatType", str]
    ] = Field(
        default=None,
        description="The format of the book.",
    )
    isbn: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The ISBN of the book.",
    )
    illustrator: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="The illustrator of the book.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Integer import Integer
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Boolean import Boolean
    from pydantic2_schemaorg.BookFormatType import BookFormatType
    from pydantic2_schemaorg.Person import Person
