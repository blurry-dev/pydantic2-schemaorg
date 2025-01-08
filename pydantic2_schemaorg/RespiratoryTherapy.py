from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalTherapy import MedicalTherapy
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty


class RespiratoryTherapy(MedicalTherapy, MedicalSpecialty):
    """The therapy that is concerned with the maintenance or improvement of respiratory function (as in patients
     with pulmonary disease).

    See: https://schema.org/RespiratoryTherapy
    Model depth: 6
    """

    type_: str = Field(default="RespiratoryTherapy", alias="@type", const=True)
