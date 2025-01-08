from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.FinancialService import FinancialService


class AutomatedTeller(FinancialService):
    """ATM/cash machine.

    See: https://schema.org/AutomatedTeller
    Model depth: 5
    """

    type_: str = Field(default="AutomatedTeller", alias="@type", const=True)
