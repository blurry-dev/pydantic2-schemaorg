from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PhysicalExam import PhysicalExam


class Throat(PhysicalExam):
    """Throat assessment with clinical examination.

    See: https://schema.org/Throat
    Model depth: 5
    """

    type_: str = Field(default="Throat", alias="@type", const=True)
