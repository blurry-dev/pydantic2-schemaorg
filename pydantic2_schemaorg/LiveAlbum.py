from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class LiveAlbum(MusicAlbumProductionType):
    """LiveAlbum.

    See: https://schema.org/LiveAlbum
    Model depth: 5
    """

    type_: str = Field(default="LiveAlbum", alias="@type", const=True)
