from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType


class SingleRelease(MusicAlbumReleaseType):
    """SingleRelease.

    See: https://schema.org/SingleRelease
    Model depth: 5
    """

    type_: str = Field(default="SingleRelease", alias="@type", const=True)
