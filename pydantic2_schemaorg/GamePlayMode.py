from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class GamePlayMode(Enumeration):
    """Indicates whether this game is multi-player, co-op or single-player.

    See: https://schema.org/GamePlayMode
    Model depth: 4
    """

    type_: str = Field(default="GamePlayMode", alias="@type", const=True)
