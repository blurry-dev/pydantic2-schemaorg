from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEnumeration import MedicalEnumeration


class DrugCostCategory(MedicalEnumeration):
    """Enumerated categories of medical drug costs.

    See: https://schema.org/DrugCostCategory
    Model depth: 5
    """

    type_: str = Field(default="DrugCostCategory", alias="@type", const=True)
