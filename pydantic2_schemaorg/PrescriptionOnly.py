from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DrugPrescriptionStatus import DrugPrescriptionStatus


class PrescriptionOnly(DrugPrescriptionStatus):
    """Available by prescription only.

    See: https://schema.org/PrescriptionOnly
    Model depth: 6
    """

    type_: str = Field(default="PrescriptionOnly", alias="@type", const=True)
