from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Clip import Clip


class MovieClip(Clip):
    """A short segment/part of a movie.

    See: https://schema.org/MovieClip
    Model depth: 4
    """

    type_: str = Field(default="MovieClip", alias="@type", const=True)
