from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty


class Dentistry(MedicalSpecialty):
    """A branch of medicine that is involved in the dental care.

    See: https://schema.org/Dentistry
    Model depth: 6
    """

    type_: str = Field(default="Dentistry", alias="@type", const=True)
