from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.StatusEnumeration import StatusEnumeration


class LegalForceStatus(StatusEnumeration):
    """A list of possible statuses for the legal force of a legislation.

    See: https://schema.org/LegalForceStatus
    Model depth: 5
    """

    type_: str = Field(default="LegalForceStatus", alias="@type", const=True)
