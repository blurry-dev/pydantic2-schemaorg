from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class ContactPointOption(Enumeration):
    """Enumerated options related to a ContactPoint.

    See: https://schema.org/ContactPointOption
    Model depth: 4
    """

    type_: str = Field(default="ContactPointOption", alias="@type", const=True)
