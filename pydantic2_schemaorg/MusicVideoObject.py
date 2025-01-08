from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MediaObject import MediaObject


class MusicVideoObject(MediaObject):
    """A music video file.

    See: https://schema.org/MusicVideoObject
    Model depth: 4
    """

    type_: str = Field(default="MusicVideoObject", alias="@type", const=True)
