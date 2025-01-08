from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class BookStore(Store):
    """A bookstore.

    See: https://schema.org/BookStore
    Model depth: 5
    """

    type_: str = Field(default="BookStore", alias="@type", const=True)
