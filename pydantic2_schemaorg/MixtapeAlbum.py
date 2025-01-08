from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class MixtapeAlbum(MusicAlbumProductionType):
    """MixtapeAlbum.

    See: https://schema.org/MixtapeAlbum
    Model depth: 5
    """

    type_: str = Field(default="MixtapeAlbum", alias="@type", const=True)
