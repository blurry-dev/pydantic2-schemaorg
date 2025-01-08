from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic.v1 import AnyUrl
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.PerformingGroup import PerformingGroup


class MusicGroup(PerformingGroup):
    """A musical group, such as a band, an orchestra, or a choir. Can also be a solo musician.

    See: https://schema.org/MusicGroup
    Model depth: 4
    """

    type_: str = Field(default="MusicGroup", alias="@type", const=True)
    genre: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description="Genre of the creative work, broadcast channel or group.",
    )
    musicGroupMember: Optional[Union[List[Union["Person", str]], "Person", str]] = (
        Field(
            default=None,
            description="A member of a music group&#x2014;for example, John, Paul, George, or Ringo.",
        )
    )
    albums: Optional[Union[List[Union["MusicAlbum", str]], "MusicAlbum", str]] = Field(
        default=None,
        description="A collection of music albums.",
    )
    tracks: Optional[
        Union[List[Union["MusicRecording", str]], "MusicRecording", str]
    ] = Field(
        default=None,
        description="A music recording (track)&#x2014;usually a single song.",
    )
    album: Optional[Union[List[Union["MusicAlbum", str]], "MusicAlbum", str]] = Field(
        default=None,
        description="A music album.",
    )
    track: Optional[
        Union[
            List[Union["ItemList", "MusicRecording", str]],
            "ItemList",
            "MusicRecording",
            str,
        ]
    ] = Field(
        default=None,
        description="A music recording (track)&#x2014;usually a single song. If an ItemList is given, the list should contain items of type MusicRecording.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.MusicAlbum import MusicAlbum
    from pydantic2_schemaorg.MusicRecording import MusicRecording
    from pydantic2_schemaorg.ItemList import ItemList
