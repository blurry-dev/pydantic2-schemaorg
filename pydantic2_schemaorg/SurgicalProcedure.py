from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalProcedure import MedicalProcedure


class SurgicalProcedure(MedicalProcedure):
    """A medical procedure involving an incision with instruments; performed for diagnose, or therapeutic purposes.

    See: https://schema.org/SurgicalProcedure
    Model depth: 4
    """

    type_: str = Field(default="SurgicalProcedure", alias="@type", const=True)
