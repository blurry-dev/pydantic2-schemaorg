from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PaymentStatusType import PaymentStatusType


class PaymentDue(PaymentStatusType):
    """The payment is due, but still within an acceptable time to be received.

    See: https://schema.org/PaymentDue
    Model depth: 6
    """

    type_: str = Field(default="PaymentDue", alias="@type", const=True)
