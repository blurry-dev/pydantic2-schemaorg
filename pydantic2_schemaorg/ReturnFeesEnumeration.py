from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class ReturnFeesEnumeration(Enumeration):
    """Enumerates several kinds of policies for product return fees.

    See: https://schema.org/ReturnFeesEnumeration
    Model depth: 4
    """

    type_: str = Field(default="ReturnFeesEnumeration", alias="@type", const=True)
