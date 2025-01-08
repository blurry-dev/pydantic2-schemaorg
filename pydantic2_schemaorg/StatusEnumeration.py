from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class StatusEnumeration(Enumeration):
    """Lists or enumerations dealing with status types.

    See: https://schema.org/StatusEnumeration
    Model depth: 4
    """

    type_: str = Field(default="StatusEnumeration", alias="@type", const=True)
