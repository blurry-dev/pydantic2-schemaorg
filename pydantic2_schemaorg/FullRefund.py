from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.RefundTypeEnumeration import RefundTypeEnumeration


class FullRefund(RefundTypeEnumeration):
    """Specifies that a refund can be done in the full amount the customer paid for the product.

    See: https://schema.org/FullRefund
    Model depth: 5
    """

    type_: str = Field(default="FullRefund", alias="@type", const=True)
