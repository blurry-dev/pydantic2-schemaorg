from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic2_schemaorg.MedicalOrganization import MedicalOrganization
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class Dentist(MedicalBusiness, MedicalOrganization, LocalBusiness):
    """A dentist.

    See: https://schema.org/Dentist
    Model depth: 4
    """

    type_: str = Field(default="Dentist", alias="@type", const=True)
