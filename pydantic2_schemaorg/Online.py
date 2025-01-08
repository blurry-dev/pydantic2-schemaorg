from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GameServerStatus import GameServerStatus


class Online(GameServerStatus):
    """Game server status: Online. Server is available.

    See: https://schema.org/Online
    Model depth: 6
    """

    type_: str = Field(default="Online", alias="@type", const=True)
