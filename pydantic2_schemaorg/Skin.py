from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PhysicalExam import PhysicalExam


class Skin(PhysicalExam):
    """Skin assessment with clinical examination.

    See: https://schema.org/Skin
    Model depth: 5
    """

    type_: str = Field(default="Skin", alias="@type", const=True)
