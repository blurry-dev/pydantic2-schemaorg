from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Message import Message


class EmailMessage(Message):
    """An email message.

    See: https://schema.org/EmailMessage
    Model depth: 4
    """

    type_: str = Field(default="EmailMessage", alias="@type", const=True)
