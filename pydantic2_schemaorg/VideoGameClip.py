from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Clip import Clip


class VideoGameClip(Clip):
    """A short segment/part of a video game.

    See: https://schema.org/VideoGameClip
    Model depth: 4
    """

    type_: str = Field(default="VideoGameClip", alias="@type", const=True)
