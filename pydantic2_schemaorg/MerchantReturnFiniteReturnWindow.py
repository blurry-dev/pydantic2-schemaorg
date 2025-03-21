from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnFiniteReturnWindow(MerchantReturnEnumeration):
    """Specifies that there is a finite window for product returns.

    See: https://schema.org/MerchantReturnFiniteReturnWindow
    Model depth: 5
    """

    type_: str = Field(
        default="MerchantReturnFiniteReturnWindow", alias="@type", const=True
    )
