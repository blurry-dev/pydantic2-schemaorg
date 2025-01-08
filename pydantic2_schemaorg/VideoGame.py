from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl


from pydantic.v1 import Field
from pydantic2_schemaorg.Game import Game
from pydantic2_schemaorg.SoftwareApplication import SoftwareApplication


class VideoGame(Game, SoftwareApplication):
    """A video game is an electronic game that involves human interaction with a user interface to generate visual
     feedback on a video device.

    See: https://schema.org/VideoGame
    Model depth: 4
    """

    type_: str = Field(default="VideoGame", alias="@type", const=True)
    trailer: Optional[Union[List[Union["VideoObject", str]], "VideoObject", str]] = (
        Field(
            default=None,
            description="The trailer of a movie or TV/radio series, season, episode, etc.",
        )
    )
    playMode: Optional[Union[List[Union["GamePlayMode", str]], "GamePlayMode", str]] = (
        Field(
            default=None,
            description="Indicates whether this game is multi-player, co-op or single-player. The game can be marked as multi-player, co-op and single-player at the same time.",
        )
    )
    gameEdition: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The edition of a video game.",
    )
    actors: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.",
    )
    gameServer: Optional[Union[List[Union["GameServer", str]], "GameServer", str]] = (
        Field(
            default=None,
            description="The server on which it is possible to play the game.",
        )
    )
    director: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.",
    )
    directors: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.",
    )
    cheatCode: Optional[
        Union[List[Union["CreativeWork", str]], "CreativeWork", str]
    ] = Field(
        default=None,
        description="Cheat codes to the game.",
    )
    gameTip: Optional[Union[List[Union["CreativeWork", str]], "CreativeWork", str]] = (
        Field(
            default=None,
            description="Links to tips, tactics, etc.",
        )
    )
    gamePlatform: Optional[
        Union[
            List[Union[AnyUrl, "URL", str, "Text", "Thing"]],
            AnyUrl,
            "URL",
            str,
            "Text",
            "Thing",
        ]
    ] = Field(
        default=None,
        description='The electronic systems used to play <a href="http://en.wikipedia.org/wiki/Category:Video_game_platforms">video games</a>.',
    )
    actor: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.",
    )
    musicBy: Optional[
        Union[List[Union["Person", "MusicGroup", str]], "Person", "MusicGroup", str]
    ] = Field(
        default=None,
        description="The composer of the soundtrack.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.VideoObject import VideoObject
    from pydantic2_schemaorg.GamePlayMode import GamePlayMode
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.GameServer import GameServer
    from pydantic2_schemaorg.CreativeWork import CreativeWork
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.Thing import Thing
    from pydantic2_schemaorg.MusicGroup import MusicGroup
