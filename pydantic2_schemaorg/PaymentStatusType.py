from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.StatusEnumeration import StatusEnumeration


class PaymentStatusType(StatusEnumeration):
    """A specific payment status. For example, PaymentDue, PaymentComplete, etc.

    See: https://schema.org/PaymentStatusType
    Model depth: 5
    """

    type_: str = Field(default="PaymentStatusType", alias="@type", const=True)
