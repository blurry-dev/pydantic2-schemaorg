from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PhysicalExam import PhysicalExam


class Appearance(PhysicalExam):
    """Appearance assessment with clinical examination.

    See: https://schema.org/Appearance
    Model depth: 5
    """

    type_: str = Field(default="Appearance", alias="@type", const=True)
