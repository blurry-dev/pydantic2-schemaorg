from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty


class PharmacySpecialty(MedicalSpecialty):
    """The practice or art and science of preparing and dispensing drugs and medicines.

    See: https://schema.org/PharmacySpecialty
    Model depth: 6
    """

    type_: str = Field(default="PharmacySpecialty", alias="@type", const=True)
