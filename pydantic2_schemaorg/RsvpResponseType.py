from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class RsvpResponseType(Enumeration):
    """RsvpResponseType is an enumeration type whose instances represent responding to an RSVP request.

    See: https://schema.org/RsvpResponseType
    Model depth: 4
    """

    type_: str = Field(default="RsvpResponseType", alias="@type", const=True)
