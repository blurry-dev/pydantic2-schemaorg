from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class ArtGallery(EntertainmentBusiness):
    """An art gallery.

    See: https://schema.org/ArtGallery
    Model depth: 5
    """

    type_: str = Field(default="ArtGallery", alias="@type", const=True)
