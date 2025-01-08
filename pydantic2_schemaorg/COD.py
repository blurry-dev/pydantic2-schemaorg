from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PaymentMethodType import PaymentMethodType


class COD(PaymentMethodType):
    """Cash on Delivery (COD) payment, equivalent to <code>http://purl.org/goodrelations/v1#COD</code>.

    See: https://schema.org/COD
    Model depth: 5
    """

    type_: str = Field(default="COD", alias="@type", const=True)
