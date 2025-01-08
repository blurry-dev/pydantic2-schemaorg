from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DigitalDocumentPermissionType import (
    DigitalDocumentPermissionType,
)


class ReadPermission(DigitalDocumentPermissionType):
    """Permission to read or view the document.

    See: https://schema.org/ReadPermission
    Model depth: 5
    """

    type_: str = Field(default="ReadPermission", alias="@type", const=True)
