from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ReturnMethodEnumeration import ReturnMethodEnumeration


class ReturnAtKiosk(ReturnMethodEnumeration):
    """Specifies that product returns must be made at a kiosk.

    See: https://schema.org/ReturnAtKiosk
    Model depth: 5
    """

    type_: str = Field(default="ReturnAtKiosk", alias="@type", const=True)
