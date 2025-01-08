from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.FinancialService import FinancialService


class BankOrCreditUnion(FinancialService):
    """Bank or credit union.

    See: https://schema.org/BankOrCreditUnion
    Model depth: 5
    """

    type_: str = Field(default="BankOrCreditUnion", alias="@type", const=True)
