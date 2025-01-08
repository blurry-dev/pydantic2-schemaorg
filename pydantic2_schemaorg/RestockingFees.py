from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration


class RestockingFees(ReturnFeesEnumeration):
    """Specifies that the customer must pay a restocking fee when returning a product.

    See: https://schema.org/RestockingFees
    Model depth: 5
    """

    type_: str = Field(default="RestockingFees", alias="@type", const=True)
