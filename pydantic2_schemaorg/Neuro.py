from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PhysicalExam import PhysicalExam


class Neuro(PhysicalExam):
    """Neurological system clinical examination.

    See: https://schema.org/Neuro
    Model depth: 5
    """

    type_: str = Field(default="Neuro", alias="@type", const=True)
