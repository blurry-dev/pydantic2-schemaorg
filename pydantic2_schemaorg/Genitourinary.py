from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PhysicalExam import PhysicalExam


class Genitourinary(PhysicalExam):
    """Genitourinary system function assessment with clinical examination.

    See: https://schema.org/Genitourinary
    Model depth: 5
    """

    type_: str = Field(default="Genitourinary", alias="@type", const=True)
