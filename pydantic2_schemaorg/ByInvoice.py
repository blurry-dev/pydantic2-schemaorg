from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PaymentMethodType import PaymentMethodType


class ByInvoice(PaymentMethodType):
    """Payment by invoice, typically after the goods were delivered, equivalent to <code>http://purl.org/goodrelations/v1#ByInvoice</code>.

    See: https://schema.org/ByInvoice
    Model depth: 5
    """

    type_: str = Field(default="ByInvoice", alias="@type", const=True)
