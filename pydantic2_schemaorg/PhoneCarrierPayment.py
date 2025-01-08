from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PaymentMethodType import PaymentMethodType


class PhoneCarrierPayment(PaymentMethodType):
    """Payment by billing via the phone carrier.

    See: https://schema.org/PhoneCarrierPayment
    Model depth: 5
    """

    type_: str = Field(default="PhoneCarrierPayment", alias="@type", const=True)
