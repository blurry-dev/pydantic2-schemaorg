from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PaymentMethodType import PaymentMethodType


class ByBankTransferInAdvance(PaymentMethodType):
    """Payment in advance by bank transfer, equivalent to <code>http://purl.org/goodrelations/v1#ByBankTransferInAdvance</code>.

    See: https://schema.org/ByBankTransferInAdvance
    Model depth: 5
    """

    type_: str = Field(default="ByBankTransferInAdvance", alias="@type", const=True)
