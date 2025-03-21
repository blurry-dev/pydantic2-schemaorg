from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class DemoAlbum(MusicAlbumProductionType):
    """DemoAlbum.

    See: https://schema.org/DemoAlbum
    Model depth: 5
    """

    type_: str = Field(default="DemoAlbum", alias="@type", const=True)
