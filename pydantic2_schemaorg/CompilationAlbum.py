from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class CompilationAlbum(MusicAlbumProductionType):
    """CompilationAlbum.

    See: https://schema.org/CompilationAlbum
    Model depth: 5
    """

    type_: str = Field(default="CompilationAlbum", alias="@type", const=True)
