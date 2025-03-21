from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnNotPermitted(MerchantReturnEnumeration):
    """Specifies that product returns are not permitted.

    See: https://schema.org/MerchantReturnNotPermitted
    Model depth: 5
    """

    type_: str = Field(default="MerchantReturnNotPermitted", alias="@type", const=True)
