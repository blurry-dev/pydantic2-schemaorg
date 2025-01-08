from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.FinancialProduct import FinancialProduct


class CurrencyConversionService(FinancialProduct):
    """A service to convert funds from one currency to another currency.

    See: https://schema.org/CurrencyConversionService
    Model depth: 5
    """

    type_: str = Field(default="CurrencyConversionService", alias="@type", const=True)
