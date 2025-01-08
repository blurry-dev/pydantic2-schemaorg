from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicineSystem import MedicineSystem


class Osteopathic(MedicineSystem):
    """A system of medicine focused on promoting the body's innate ability to heal itself.

    See: https://schema.org/Osteopathic
    Model depth: 6
    """

    type_: str = Field(default="Osteopathic", alias="@type", const=True)
