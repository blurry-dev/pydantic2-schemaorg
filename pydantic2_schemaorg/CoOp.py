from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GamePlayMode import GamePlayMode


class CoOp(GamePlayMode):
    """Play mode: CoOp. Co-operative games, where you play on the same team with friends.

    See: https://schema.org/CoOp
    Model depth: 5
    """

    type_: str = Field(default="CoOp", alias="@type", const=True)
