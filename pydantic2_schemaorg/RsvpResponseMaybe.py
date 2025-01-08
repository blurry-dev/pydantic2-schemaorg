from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.RsvpResponseType import RsvpResponseType


class RsvpResponseMaybe(RsvpResponseType):
    """The invitee may or may not attend.

    See: https://schema.org/RsvpResponseMaybe
    Model depth: 5
    """

    type_: str = Field(default="RsvpResponseMaybe", alias="@type", const=True)
