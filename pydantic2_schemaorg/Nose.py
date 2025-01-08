from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PhysicalExam import PhysicalExam


class Nose(PhysicalExam):
    """Nose function assessment with clinical examination.

    See: https://schema.org/Nose
    Model depth: 5
    """

    type_: str = Field(default="Nose", alias="@type", const=True)
