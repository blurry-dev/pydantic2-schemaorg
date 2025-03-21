from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnUnlimitedWindow(MerchantReturnEnumeration):
    """Specifies that there is an unlimited window for product returns.

    See: https://schema.org/MerchantReturnUnlimitedWindow
    Model depth: 5
    """

    type_: str = Field(
        default="MerchantReturnUnlimitedWindow", alias="@type", const=True
    )
