from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.FinancialService import FinancialService


class AccountingService(FinancialService):
    """Accountancy business. As a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]](s).

    See: https://schema.org/AccountingService
    Model depth: 5
    """

    type_: str = Field(default="AccountingService", alias="@type", const=True)
