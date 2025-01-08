from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GameServerStatus import GameServerStatus


class OnlineFull(GameServerStatus):
    """Game server status: OnlineFull. Server is online but unavailable. The maximum number of players has reached.

    See: https://schema.org/OnlineFull
    Model depth: 6
    """

    type_: str = Field(default="OnlineFull", alias="@type", const=True)
