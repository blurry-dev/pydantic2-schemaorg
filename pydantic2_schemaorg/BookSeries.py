from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWorkSeries import CreativeWorkSeries


class BookSeries(CreativeWorkSeries):
    """A series of books. Included books can be indicated with the hasPart property.

    See: https://schema.org/BookSeries
    Model depth: 4
    """

    type_: str = Field(default="BookSeries", alias="@type", const=True)
