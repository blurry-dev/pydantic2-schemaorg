from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class ReturnMethodEnumeration(Enumeration):
    """Enumerates several types of product return methods.

    See: https://schema.org/ReturnMethodEnumeration
    Model depth: 4
    """

    type_: str = Field(default="ReturnMethodEnumeration", alias="@type", const=True)
