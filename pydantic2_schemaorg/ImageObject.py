from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic.v1 import StrictBool
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.MediaObject import MediaObject


class ImageObject(MediaObject):
    """An image file.

    See: https://schema.org/ImageObject
    Model depth: 4
    """

    type_: str = Field(default="ImageObject", alias="@type", const=True)
    representativeOfPage: Optional[
        Union[List[Union[StrictBool, "Boolean", str]], StrictBool, "Boolean", str]
    ] = Field(
        default=None,
        description="Indicates whether this image is representative of the content of the page.",
    )
    exifData: Optional[
        Union[List[Union[str, "Text", "PropertyValue"]], str, "Text", "PropertyValue"]
    ] = Field(
        default=None,
        description="exif data for this object.",
    )
    embeddedTextCaption: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.",
    )
    caption: Optional[
        Union[List[Union[str, "Text", "MediaObject"]], str, "Text", "MediaObject"]
    ] = Field(
        default=None,
        description="The caption for this object. For downloadable machine formats (closed caption, subtitles etc.) use MediaObject and indicate the [[encodingFormat]].",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Boolean import Boolean
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.PropertyValue import PropertyValue
    from pydantic2_schemaorg.MediaObject import MediaObject
