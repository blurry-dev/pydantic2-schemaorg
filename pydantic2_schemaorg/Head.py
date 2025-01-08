from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PhysicalExam import PhysicalExam


class Head(PhysicalExam):
    """Head assessment with clinical examination.

    See: https://schema.org/Head
    Model depth: 5
    """

    type_: str = Field(default="Head", alias="@type", const=True)
