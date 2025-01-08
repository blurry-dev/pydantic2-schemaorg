from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GamePlayMode import GamePlayMode


class SinglePlayer(GamePlayMode):
    """Play mode: SinglePlayer. Which is played by a lone player.

    See: https://schema.org/SinglePlayer
    Model depth: 5
    """

    type_: str = Field(default="SinglePlayer", alias="@type", const=True)
