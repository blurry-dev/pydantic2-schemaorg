from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class PaymentMethod(Intangible):
    """A payment method is a standardized procedure for transferring the monetary amount for a purchase. Payment
     methods are characterized by the legal and technical structures used, and by the organization or group carrying
     out the transaction. The following legacy values should be accepted: * http://purl.org/goodrelations/v1#ByBankTransferInAdvance
     * http://purl.org/goodrelations/v1#ByInvoice * http://purl.org/goodrelations/v1#Cash * http://purl.org/goodrelations/v1#CheckInAdvance
     * http://purl.org/goodrelations/v1#COD * http://purl.org/goodrelations/v1#DirectDebit * http://purl.org/goodrelations/v1#GoogleCheckout
     * http://purl.org/goodrelations/v1#PayPal * http://purl.org/goodrelations/v1#PaySwarm Structured
     values are recommended for newer payment methods.

    See: https://schema.org/PaymentMethod
    Model depth: 3
    """

    type_: str = Field(default="PaymentMethod", alias="@type", const=True)
    paymentMethodType: Optional[
        Union[List[Union["PaymentMethodType", str]], "PaymentMethodType", str]
    ] = Field(
        default=None,
        description="The type of a payment method.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.PaymentMethodType import PaymentMethodType
