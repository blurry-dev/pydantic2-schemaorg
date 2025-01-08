from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic2_schemaorg.MedicalBusiness import MedicalBusiness


class Emergency(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that deals with the evaluation and initial treatment of medical conditions
     caused by trauma or sudden illness.

    See: https://schema.org/Emergency
    Model depth: 5
    """

    type_: str = Field(default="Emergency", alias="@type", const=True)
