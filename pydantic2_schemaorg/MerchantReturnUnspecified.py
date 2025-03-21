from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnUnspecified(MerchantReturnEnumeration):
    """Specifies that a product return policy is not provided.

    See: https://schema.org/MerchantReturnUnspecified
    Model depth: 5
    """

    type_: str = Field(default="MerchantReturnUnspecified", alias="@type", const=True)
