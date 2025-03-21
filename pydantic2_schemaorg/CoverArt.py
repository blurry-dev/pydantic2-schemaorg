from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.VisualArtwork import VisualArtwork


class CoverArt(VisualArtwork):
    """The artwork on the outer surface of a CreativeWork.

    See: https://schema.org/CoverArt
    Model depth: 4
    """

    type_: str = Field(default="CoverArt", alias="@type", const=True)
