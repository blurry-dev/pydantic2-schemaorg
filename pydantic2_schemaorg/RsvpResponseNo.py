from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.RsvpResponseType import RsvpResponseType


class RsvpResponseNo(RsvpResponseType):
    """The invitee will not attend.

    See: https://schema.org/RsvpResponseNo
    Model depth: 5
    """

    type_: str = Field(default="RsvpResponseNo", alias="@type", const=True)
