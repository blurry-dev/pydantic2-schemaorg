from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic2_schemaorg.MedicalOrganization import MedicalOrganization


class Pharmacy(MedicalBusiness, MedicalOrganization):
    """A pharmacy or drugstore.

    See: https://schema.org/Pharmacy
    Model depth: 4
    """

    type_: str = Field(default="Pharmacy", alias="@type", const=True)
