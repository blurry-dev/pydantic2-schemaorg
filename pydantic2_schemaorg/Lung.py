from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PhysicalExam import PhysicalExam


class Lung(PhysicalExam):
    """Lung and respiratory system clinical examination.

    See: https://schema.org/Lung
    Model depth: 5
    """

    type_: str = Field(default="Lung", alias="@type", const=True)
