from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Event import Event


class SocialEvent(Event):
    """Event type: Social event.

    See: https://schema.org/SocialEvent
    Model depth: 3
    """

    type_: str = Field(default="SocialEvent", alias="@type", const=True)
