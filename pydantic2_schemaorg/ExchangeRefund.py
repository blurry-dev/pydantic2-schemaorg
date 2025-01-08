from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.RefundTypeEnumeration import RefundTypeEnumeration


class ExchangeRefund(RefundTypeEnumeration):
    """Specifies that a refund can be done as an exchange for the same product.

    See: https://schema.org/ExchangeRefund
    Model depth: 5
    """

    type_: str = Field(default="ExchangeRefund", alias="@type", const=True)
