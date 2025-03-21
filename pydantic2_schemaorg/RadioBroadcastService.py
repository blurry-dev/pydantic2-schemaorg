from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BroadcastService import BroadcastService


class RadioBroadcastService(BroadcastService):
    """A delivery service through which radio content is provided via broadcast over the air or online.

    See: https://schema.org/RadioBroadcastService
    Model depth: 5
    """

    type_: str = Field(default="RadioBroadcastService", alias="@type", const=True)
