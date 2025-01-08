from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DrugCostCategory import DrugCostCategory


class ReimbursementCap(DrugCostCategory):
    """The drug's cost represents the maximum reimbursement paid by an insurer for the drug.

    See: https://schema.org/ReimbursementCap
    Model depth: 6
    """

    type_: str = Field(default="ReimbursementCap", alias="@type", const=True)
