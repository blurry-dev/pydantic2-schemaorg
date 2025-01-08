from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class ShortStory(CreativeWork):
    """Short story or tale. A brief work of literature, usually written in narrative prose.

    See: https://schema.org/ShortStory
    Model depth: 3
    """

    type_: str = Field(default="ShortStory", alias="@type", const=True)
