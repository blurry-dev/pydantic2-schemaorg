from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AnatomicalStructure import AnatomicalStructure


class Bone(AnatomicalStructure):
    """Rigid connective tissue that comprises up the skeletal structure of the human body.

    See: https://schema.org/Bone
    Model depth: 4
    """

    type_: str = Field(default="Bone", alias="@type", const=True)
