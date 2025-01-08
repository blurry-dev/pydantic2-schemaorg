from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DrugPregnancyCategory import DrugPregnancyCategory


class FDAnotEvaluated(DrugPregnancyCategory):
    """A designation that the drug in question has not been assigned a pregnancy category designation by the US FDA.

    See: https://schema.org/FDAnotEvaluated
    Model depth: 6
    """

    type_: str = Field(default="FDAnotEvaluated", alias="@type", const=True)
