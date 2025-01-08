from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.RsvpResponseType import RsvpResponseType


class RsvpResponseYes(RsvpResponseType):
    """The invitee will attend.

    See: https://schema.org/RsvpResponseYes
    Model depth: 5
    """

    type_: str = Field(default="RsvpResponseYes", alias="@type", const=True)
