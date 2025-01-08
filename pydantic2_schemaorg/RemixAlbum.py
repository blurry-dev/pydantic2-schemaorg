from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class RemixAlbum(MusicAlbumProductionType):
    """RemixAlbum.

    See: https://schema.org/RemixAlbum
    Model depth: 5
    """

    type_: str = Field(default="RemixAlbum", alias="@type", const=True)
