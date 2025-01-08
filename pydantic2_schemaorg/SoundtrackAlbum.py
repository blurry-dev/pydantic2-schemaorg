from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class SoundtrackAlbum(MusicAlbumProductionType):
    """SoundtrackAlbum.

    See: https://schema.org/SoundtrackAlbum
    Model depth: 5
    """

    type_: str = Field(default="SoundtrackAlbum", alias="@type", const=True)
