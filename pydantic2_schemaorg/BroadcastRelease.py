from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType


class BroadcastRelease(MusicAlbumReleaseType):
    """BroadcastRelease.

    See: https://schema.org/BroadcastRelease
    Model depth: 5
    """

    type_: str = Field(default="BroadcastRelease", alias="@type", const=True)
