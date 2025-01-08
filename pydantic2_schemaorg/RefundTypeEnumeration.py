from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class RefundTypeEnumeration(Enumeration):
    """Enumerates several kinds of product return refund types.

    See: https://schema.org/RefundTypeEnumeration
    Model depth: 4
    """

    type_: str = Field(default="RefundTypeEnumeration", alias="@type", const=True)
