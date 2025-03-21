from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GamePlayMode import GamePlayMode


class MultiPlayer(GamePlayMode):
    """Play mode: MultiPlayer. Requiring or allowing multiple human players to play simultaneously.

    See: https://schema.org/MultiPlayer
    Model depth: 5
    """

    type_: str = Field(default="MultiPlayer", alias="@type", const=True)
