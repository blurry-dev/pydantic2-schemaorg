from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import date, datetime
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class Message(CreativeWork):
    """A single message from a sender to one or more organizations or people.

    See: https://schema.org/Message
    Model depth: 3
    """

    type_: str = Field(default="Message", alias="@type", const=True)
    dateSent: Optional[
        Union[List[Union[datetime, "DateTime", str]], datetime, "DateTime", str]
    ] = Field(
        default=None,
        description="The date/time at which the message was sent.",
    )
    bccRecipient: Optional[
        Union[
            List[Union["Organization", "Person", "ContactPoint", str]],
            "Organization",
            "Person",
            "ContactPoint",
            str,
        ]
    ] = Field(
        default=None,
        description="A sub property of recipient. The recipient blind copied on a message.",
    )
    recipient: Optional[
        Union[
            List[Union["Organization", "Audience", "Person", "ContactPoint", str]],
            "Organization",
            "Audience",
            "Person",
            "ContactPoint",
            str,
        ]
    ] = Field(
        default=None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    dateRead: Optional[
        Union[
            List[Union[datetime, "DateTime", date, "Date", str]],
            datetime,
            "DateTime",
            date,
            "Date",
            str,
        ]
    ] = Field(
        default=None,
        description="The date/time at which the message has been read by the recipient if a single recipient exists.",
    )
    dateReceived: Optional[
        Union[List[Union[datetime, "DateTime", str]], datetime, "DateTime", str]
    ] = Field(
        default=None,
        description="The date/time the message was received if a single recipient exists.",
    )
    messageAttachment: Optional[
        Union[List[Union["CreativeWork", str]], "CreativeWork", str]
    ] = Field(
        default=None,
        description="A CreativeWork attached to the message.",
    )
    sender: Optional[
        Union[
            List[Union["Audience", "Person", "Organization", str]],
            "Audience",
            "Person",
            "Organization",
            str,
        ]
    ] = Field(
        default=None,
        description="A sub property of participant. The participant who is at the sending end of the action.",
    )
    toRecipient: Optional[
        Union[
            List[Union["ContactPoint", "Audience", "Person", "Organization", str]],
            "ContactPoint",
            "Audience",
            "Person",
            "Organization",
            str,
        ]
    ] = Field(
        default=None,
        description="A sub property of recipient. The recipient who was directly sent the message.",
    )
    ccRecipient: Optional[
        Union[
            List[Union["ContactPoint", "Person", "Organization", str]],
            "ContactPoint",
            "Person",
            "Organization",
            str,
        ]
    ] = Field(
        default=None,
        description="A sub property of recipient. The recipient copied on a message.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.ContactPoint import ContactPoint
    from pydantic2_schemaorg.Audience import Audience
    from pydantic2_schemaorg.Date import Date
    from pydantic2_schemaorg.CreativeWork import CreativeWork
