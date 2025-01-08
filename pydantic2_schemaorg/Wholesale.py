from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DrugCostCategory import DrugCostCategory


class Wholesale(DrugCostCategory):
    """The drug's cost represents the wholesale acquisition cost of the drug.

    See: https://schema.org/Wholesale
    Model depth: 6
    """

    type_: str = Field(default="Wholesale", alias="@type", const=True)
