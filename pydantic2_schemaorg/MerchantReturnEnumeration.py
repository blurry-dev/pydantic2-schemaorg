from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class MerchantReturnEnumeration(Enumeration):
    """Enumerates several kinds of product return policies.

    See: https://schema.org/MerchantReturnEnumeration
    Model depth: 4
    """

    type_: str = Field(default="MerchantReturnEnumeration", alias="@type", const=True)
