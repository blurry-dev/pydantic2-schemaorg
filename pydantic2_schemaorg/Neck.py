from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PhysicalExam import PhysicalExam


class Neck(PhysicalExam):
    """Neck assessment with clinical examination.

    See: https://schema.org/Neck
    Model depth: 5
    """

    type_: str = Field(default="Neck", alias="@type", const=True)
