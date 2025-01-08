from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType


class AlbumRelease(MusicAlbumReleaseType):
    """AlbumRelease.

    See: https://schema.org/AlbumRelease
    Model depth: 5
    """

    type_: str = Field(default="AlbumRelease", alias="@type", const=True)
