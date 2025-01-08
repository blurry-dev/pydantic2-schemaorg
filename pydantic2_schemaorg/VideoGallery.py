from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MediaGallery import MediaGallery


class VideoGallery(MediaGallery):
    """Web page type: Video gallery page.

    See: https://schema.org/VideoGallery
    Model depth: 6
    """

    type_: str = Field(default="VideoGallery", alias="@type", const=True)
