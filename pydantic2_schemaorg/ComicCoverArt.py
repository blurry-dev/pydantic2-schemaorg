from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CoverArt import CoverArt
from pydantic2_schemaorg.ComicStory import ComicStory


class ComicCoverArt(CoverArt, ComicStory):
    """The artwork on the cover of a comic.

    See: https://schema.org/ComicCoverArt
    Model depth: 4
    """

    type_: str = Field(default="ComicCoverArt", alias="@type", const=True)
