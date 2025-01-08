from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType


class EPRelease(MusicAlbumReleaseType):
    """EPRelease.

    See: https://schema.org/EPRelease
    Model depth: 5
    """

    type_: str = Field(default="EPRelease", alias="@type", const=True)
