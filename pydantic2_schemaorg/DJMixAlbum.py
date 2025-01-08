from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class DJMixAlbum(MusicAlbumProductionType):
    """DJMixAlbum.

    See: https://schema.org/DJMixAlbum
    Model depth: 5
    """

    type_: str = Field(default="DJMixAlbum", alias="@type", const=True)
