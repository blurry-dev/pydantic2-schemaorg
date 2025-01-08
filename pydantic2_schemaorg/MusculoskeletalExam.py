from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PhysicalExam import PhysicalExam


class MusculoskeletalExam(PhysicalExam):
    """Musculoskeletal system clinical examination.

    See: https://schema.org/MusculoskeletalExam
    Model depth: 5
    """

    type_: str = Field(default="MusculoskeletalExam", alias="@type", const=True)
