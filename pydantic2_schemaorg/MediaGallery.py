from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CollectionPage import CollectionPage


class MediaGallery(CollectionPage):
    """Web page type: Media gallery page. A mixed-media page that can contain media such as images, videos, and other
     multimedia.

    See: https://schema.org/MediaGallery
    Model depth: 5
    """

    type_: str = Field(default="MediaGallery", alias="@type", const=True)
