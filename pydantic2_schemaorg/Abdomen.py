from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PhysicalExam import PhysicalExam


class Abdomen(PhysicalExam):
    """Abdomen clinical examination.

    See: https://schema.org/Abdomen
    Model depth: 5
    """

    type_: str = Field(default="Abdomen", alias="@type", const=True)
