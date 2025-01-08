from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class SheetMusic(CreativeWork):
    """Printed music, as opposed to performed or recorded music.

    See: https://schema.org/SheetMusic
    Model depth: 3
    """

    type_: str = Field(default="SheetMusic", alias="@type", const=True)
