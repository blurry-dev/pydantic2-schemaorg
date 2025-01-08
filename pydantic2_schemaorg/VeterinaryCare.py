from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalOrganization import MedicalOrganization


class VeterinaryCare(MedicalOrganization):
    """A vet's office.

    See: https://schema.org/VeterinaryCare
    Model depth: 4
    """

    type_: str = Field(default="VeterinaryCare", alias="@type", const=True)
