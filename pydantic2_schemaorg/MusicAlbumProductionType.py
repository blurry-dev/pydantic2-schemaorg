from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class MusicAlbumProductionType(Enumeration):
    """Classification of the album by its type of content: soundtrack, live album, studio album, etc.

    See: https://schema.org/MusicAlbumProductionType
    Model depth: 4
    """

    type_: str = Field(default="MusicAlbumProductionType", alias="@type", const=True)
