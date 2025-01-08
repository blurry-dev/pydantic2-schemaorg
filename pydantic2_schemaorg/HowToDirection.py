from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl


from pydantic.v1 import Field
from pydantic2_schemaorg.ListItem import ListItem
from pydantic2_schemaorg.CreativeWork import CreativeWork


class HowToDirection(ListItem, CreativeWork):
    """A direction indicating a single action to do in the instructions for how to achieve a result.

    See: https://schema.org/HowToDirection
    Model depth: 3
    """

    type_: str = Field(default="HowToDirection", alias="@type", const=True)
    supply: Optional[
        Union[List[Union[str, "Text", "HowToSupply"]], str, "Text", "HowToSupply"]
    ] = Field(
        default=None,
        description="A sub-property of instrument. A supply consumed when performing instructions or a direction.",
    )
    totalTime: Optional[Union[List[Union["Duration", str]], "Duration", str]] = Field(
        default=None,
        description="The total time required to perform instructions or a direction (including time to prepare the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    beforeMedia: Optional[
        Union[
            List[Union[AnyUrl, "URL", "MediaObject", str]],
            AnyUrl,
            "URL",
            "MediaObject",
            str,
        ]
    ] = Field(
        default=None,
        description="A media object representing the circumstances before performing this direction.",
    )
    duringMedia: Optional[
        Union[
            List[Union[AnyUrl, "URL", "MediaObject", str]],
            AnyUrl,
            "URL",
            "MediaObject",
            str,
        ]
    ] = Field(
        default=None,
        description="A media object representing the circumstances while performing this direction.",
    )
    afterMedia: Optional[
        Union[
            List[Union[AnyUrl, "URL", "MediaObject", str]],
            AnyUrl,
            "URL",
            "MediaObject",
            str,
        ]
    ] = Field(
        default=None,
        description="A media object representing the circumstances after performing this direction.",
    )
    prepTime: Optional[Union[List[Union["Duration", str]], "Duration", str]] = Field(
        default=None,
        description="The length of time it takes to prepare the items to be used in instructions or a direction, in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    performTime: Optional[Union[List[Union["Duration", str]], "Duration", str]] = Field(
        default=None,
        description="The length of time it takes to perform instructions or a direction (not including time to prepare the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    tool: Optional[
        Union[List[Union[str, "Text", "HowToTool"]], str, "Text", "HowToTool"]
    ] = Field(
        default=None,
        description="A sub property of instrument. An object used (but not consumed) when performing instructions or a direction.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.HowToSupply import HowToSupply
    from pydantic2_schemaorg.Duration import Duration
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.MediaObject import MediaObject
    from pydantic2_schemaorg.HowToTool import HowToTool
