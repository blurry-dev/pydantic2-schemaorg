from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MediaGallery import MediaGallery


class ImageGallery(MediaGallery):
    """Web page type: Image gallery page.

    See: https://schema.org/ImageGallery
    Model depth: 6
    """

    type_: str = Field(default="ImageGallery", alias="@type", const=True)
