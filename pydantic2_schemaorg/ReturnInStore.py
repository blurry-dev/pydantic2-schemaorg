from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ReturnMethodEnumeration import ReturnMethodEnumeration


class ReturnInStore(ReturnMethodEnumeration):
    """Specifies that product returns must be made in a store.

    See: https://schema.org/ReturnInStore
    Model depth: 5
    """

    type_: str = Field(default="ReturnInStore", alias="@type", const=True)
