from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PhysicalExam import PhysicalExam


class Ear(PhysicalExam):
    """Ear function assessment with clinical examination.

    See: https://schema.org/Ear
    Model depth: 5
    """

    type_: str = Field(default="Ear", alias="@type", const=True)
