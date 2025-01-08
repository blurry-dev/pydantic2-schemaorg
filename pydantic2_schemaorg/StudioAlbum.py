from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class StudioAlbum(MusicAlbumProductionType):
    """StudioAlbum.

    See: https://schema.org/StudioAlbum
    Model depth: 5
    """

    type_: str = Field(default="StudioAlbum", alias="@type", const=True)
