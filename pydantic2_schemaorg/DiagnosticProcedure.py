from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalProcedure import MedicalProcedure


class DiagnosticProcedure(MedicalProcedure):
    """A medical procedure intended primarily for diagnostic, as opposed to therapeutic, purposes.

    See: https://schema.org/DiagnosticProcedure
    Model depth: 4
    """

    type_: str = Field(default="DiagnosticProcedure", alias="@type", const=True)
