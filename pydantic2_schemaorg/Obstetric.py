from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic2_schemaorg.MedicalBusiness import MedicalBusiness


class Obstetric(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that specializes in the care of women during the prenatal and postnatal
     care and with the delivery of the child.

    See: https://schema.org/Obstetric
    Model depth: 5
    """

    type_: str = Field(default="Obstetric", alias="@type", const=True)
