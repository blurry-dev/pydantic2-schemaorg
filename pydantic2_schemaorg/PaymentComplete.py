from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PaymentStatusType import PaymentStatusType


class PaymentComplete(PaymentStatusType):
    """The payment has been received and processed.

    See: https://schema.org/PaymentComplete
    Model depth: 6
    """

    type_: str = Field(default="PaymentComplete", alias="@type", const=True)
