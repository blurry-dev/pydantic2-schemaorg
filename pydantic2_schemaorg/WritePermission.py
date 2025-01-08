from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DigitalDocumentPermissionType import (
    DigitalDocumentPermissionType,
)


class WritePermission(DigitalDocumentPermissionType):
    """Permission to write or edit the document.

    See: https://schema.org/WritePermission
    Model depth: 5
    """

    type_: str = Field(default="WritePermission", alias="@type", const=True)
