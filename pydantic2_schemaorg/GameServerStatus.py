from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.StatusEnumeration import StatusEnumeration


class GameServerStatus(StatusEnumeration):
    """Status of a game server.

    See: https://schema.org/GameServerStatus
    Model depth: 5
    """

    type_: str = Field(default="GameServerStatus", alias="@type", const=True)
