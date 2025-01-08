from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PaymentStatusType import PaymentStatusType


class PaymentPastDue(PaymentStatusType):
    """The payment is due and considered late.

    See: https://schema.org/PaymentPastDue
    Model depth: 6
    """

    type_: str = Field(default="PaymentPastDue", alias="@type", const=True)
