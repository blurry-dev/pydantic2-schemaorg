from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic2_schemaorg.MedicalBusiness import MedicalBusiness


class PlasticSurgery(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that pertains to therapeutic or cosmetic repair or re-formation of missing,
     injured or malformed tissues or body parts by manual and instrumental means.

    See: https://schema.org/PlasticSurgery
    Model depth: 5
    """

    type_: str = Field(default="PlasticSurgery", alias="@type", const=True)
