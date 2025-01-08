from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicineSystem import MedicineSystem


class Chiropractic(MedicineSystem):
    """A system of medicine focused on the relationship between the body's structure, mainly the spine, and its functioning.

    See: https://schema.org/Chiropractic
    Model depth: 6
    """

    type_: str = Field(default="Chiropractic", alias="@type", const=True)
