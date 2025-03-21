from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class ComicStory(CreativeWork):
    """The term \"story\" is any indivisible, re-printable unit of a comic, including the interior stories, covers,
     and backmatter. Most comics have at least two stories: a cover (ComicCoverArt) and an interior story.

    See: https://schema.org/ComicStory
    Model depth: 3
    """

    type_: str = Field(default="ComicStory", alias="@type", const=True)
    artist: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="The primary artist for a work in a medium other than pencils or digital line art--for example, if the primary artwork is done in watercolors or digital paints.",
    )
    inker: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="The individual who traces over the pencil drawings in ink after pencils are complete.",
    )
    letterer: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="The individual who adds lettering, including speech balloons and sound effects, to artwork.",
    )
    colorist: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="The individual who adds color to inked drawings.",
    )
    penciler: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="The individual who draws the primary narrative artwork.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Person import Person
