from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.FinancialService import FinancialService


class InsuranceAgency(FinancialService):
    """An Insurance agency.

    See: https://schema.org/InsuranceAgency
    Model depth: 5
    """

    type_: str = Field(default="InsuranceAgency", alias="@type", const=True)
