from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class MusicAlbumReleaseType(Enumeration):
    """The kind of release which this album is: single, EP or album.

    See: https://schema.org/MusicAlbumReleaseType
    Model depth: 4
    """

    type_: str = Field(default="MusicAlbumReleaseType", alias="@type", const=True)
