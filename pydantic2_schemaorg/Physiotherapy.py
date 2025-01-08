from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic2_schemaorg.MedicalBusiness import MedicalBusiness


class Physiotherapy(MedicalSpecialty, MedicalBusiness):
    """The practice of treatment of disease, injury, or deformity by physical methods such as massage, heat treatment,
     and exercise rather than by drugs or surgery.

    See: https://schema.org/Physiotherapy
    Model depth: 5
    """

    type_: str = Field(default="Physiotherapy", alias="@type", const=True)
