from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DrugPrescriptionStatus import DrugPrescriptionStatus


class OTC(DrugPrescriptionStatus):
    """The character of a medical substance, typically a medicine, of being available over the counter or not.

    See: https://schema.org/OTC
    Model depth: 6
    """

    type_: str = Field(default="OTC", alias="@type", const=True)
