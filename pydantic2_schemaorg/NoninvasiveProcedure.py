from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalProcedureType import MedicalProcedureType


class NoninvasiveProcedure(MedicalProcedureType):
    """A type of medical procedure that involves noninvasive techniques.

    See: https://schema.org/NoninvasiveProcedure
    Model depth: 6
    """

    type_: str = Field(default="NoninvasiveProcedure", alias="@type", const=True)
