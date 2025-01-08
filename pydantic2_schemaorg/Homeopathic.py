from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicineSystem import MedicineSystem


class Homeopathic(MedicineSystem):
    """A system of medicine based on the principle that a disease can be cured by a substance that produces similar
     symptoms in healthy people.

    See: https://schema.org/Homeopathic
    Model depth: 6
    """

    type_: str = Field(default="Homeopathic", alias="@type", const=True)
