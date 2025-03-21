from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DigitalDocumentPermissionType import (
    DigitalDocumentPermissionType,
)


class CommentPermission(DigitalDocumentPermissionType):
    """Permission to add comments to the document.

    See: https://schema.org/CommentPermission
    Model depth: 5
    """

    type_: str = Field(default="CommentPermission", alias="@type", const=True)
