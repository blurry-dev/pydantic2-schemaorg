from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class DigitalDocumentPermissionType(Enumeration):
    """A type of permission which can be granted for accessing a digital document.

    See: https://schema.org/DigitalDocumentPermissionType
    Model depth: 4
    """

    type_: str = Field(
        default="DigitalDocumentPermissionType", alias="@type", const=True
    )
