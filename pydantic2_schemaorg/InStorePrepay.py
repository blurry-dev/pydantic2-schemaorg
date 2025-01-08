from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PaymentMethodType import PaymentMethodType


class InStorePrepay(PaymentMethodType):
    """Payment in advance in some form of shop or kiosk for goods purchased online.

    See: https://schema.org/InStorePrepay
    Model depth: 5
    """

    type_: str = Field(default="InStorePrepay", alias="@type", const=True)
