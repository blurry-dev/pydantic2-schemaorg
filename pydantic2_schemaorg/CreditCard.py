from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LoanOrCredit import LoanOrCredit
from pydantic2_schemaorg.PaymentCard import PaymentCard


class CreditCard(LoanOrCredit, PaymentCard):
    """A card payment method of a particular brand or name. Used to mark up a particular payment method and/or the financial
     product/service that supplies the card account. Commonly used values: * http://purl.org/goodrelations/v1#AmericanExpress
     * http://purl.org/goodrelations/v1#DinersClub * http://purl.org/goodrelations/v1#Discover * http://purl.org/goodrelations/v1#JCB
     * http://purl.org/goodrelations/v1#MasterCard * http://purl.org/goodrelations/v1#VISA

    See: https://schema.org/CreditCard
    Model depth: 5
    """

    type_: str = Field(default="CreditCard", alias="@type", const=True)
