from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ContactPointOption import ContactPointOption


class HearingImpairedSupported(ContactPointOption):
    """Uses devices to support users with hearing impairments.

    See: https://schema.org/HearingImpairedSupported
    Model depth: 5
    """

    type_: str = Field(default="HearingImpairedSupported", alias="@type", const=True)
