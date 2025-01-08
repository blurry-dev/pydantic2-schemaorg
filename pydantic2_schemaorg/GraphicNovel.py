from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BookFormatType import BookFormatType


class GraphicNovel(BookFormatType):
    """Book format: GraphicNovel. May represent a bound collection of ComicIssue instances.

    See: https://schema.org/GraphicNovel
    Model depth: 5
    """

    type_: str = Field(default="GraphicNovel", alias="@type", const=True)
