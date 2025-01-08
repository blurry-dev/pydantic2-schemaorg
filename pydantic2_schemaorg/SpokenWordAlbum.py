from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class SpokenWordAlbum(MusicAlbumProductionType):
    """SpokenWordAlbum.

    See: https://schema.org/SpokenWordAlbum
    Model depth: 5
    """

    type_: str = Field(default="SpokenWordAlbum", alias="@type", const=True)
