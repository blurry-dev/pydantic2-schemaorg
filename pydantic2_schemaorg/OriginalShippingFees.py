from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration


class OriginalShippingFees(ReturnFeesEnumeration):
    """Specifies that the customer must pay the original shipping costs when returning a product.

    See: https://schema.org/OriginalShippingFees
    Model depth: 5
    """

    type_: str = Field(default="OriginalShippingFees", alias="@type", const=True)
