from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GameServerStatus import GameServerStatus


class OfflinePermanently(GameServerStatus):
    """Game server status: OfflinePermanently. Server is offline and not available.

    See: https://schema.org/OfflinePermanently
    Model depth: 6
    """

    type_: str = Field(default="OfflinePermanently", alias="@type", const=True)
