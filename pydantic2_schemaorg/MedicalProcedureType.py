from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalProcedureType(MedicalEnumeration):
    """An enumeration that describes different types of medical procedures.

    See: https://schema.org/MedicalProcedureType
    Model depth: 5
    """

    type_: str = Field(default="MedicalProcedureType", alias="@type", const=True)
