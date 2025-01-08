from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PaymentStatusType import PaymentStatusType


class PaymentDeclined(PaymentStatusType):
    """The payee received the payment, but it was declined for some reason.

    See: https://schema.org/PaymentDeclined
    Model depth: 6
    """

    type_: str = Field(default="PaymentDeclined", alias="@type", const=True)
