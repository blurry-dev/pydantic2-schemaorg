from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWorkSeries import CreativeWorkSeries


class VideoGameSeries(CreativeWorkSeries):
    """A video game series.

    See: https://schema.org/VideoGameSeries
    Model depth: 4
    """

    type_: str = Field(default="VideoGameSeries", alias="@type", const=True)
    trailer: Optional[Union[List[Union["VideoObject", str]], "VideoObject", str]] = (
        Field(
            default=None,
            description="The trailer of a movie or TV/radio series, season, episode, etc.",
        )
    )
    episode: Optional[Union[List[Union["Episode", str]], "Episode", str]] = Field(
        default=None,
        description="An episode of a TV, radio or game media within a series or season.",
    )
    numberOfEpisodes: Optional[
        Union[List[Union[int, "Integer", str]], int, "Integer", str]
    ] = Field(
        default=None,
        description="The number of episodes in this season or series.",
    )
    playMode: Optional[Union[List[Union["GamePlayMode", str]], "GamePlayMode", str]] = (
        Field(
            default=None,
            description="Indicates whether this game is multi-player, co-op or single-player. The game can be marked as multi-player, co-op and single-player at the same time.",
        )
    )
    productionCompany: Optional[
        Union[List[Union["Organization", str]], "Organization", str]
    ] = Field(
        default=None,
        description="The production company or studio responsible for the item, e.g. series, video game, episode etc.",
    )
    actors: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.",
    )
    director: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.",
    )
    season: Optional[
        Union[
            List[Union[AnyUrl, "URL", "CreativeWorkSeason", str]],
            AnyUrl,
            "URL",
            "CreativeWorkSeason",
            str,
        ]
    ] = Field(
        default=None,
        description="A season in a media series.",
    )
    gameItem: Optional[Union[List[Union["Thing", str]], "Thing", str]] = Field(
        default=None,
        description="An item is an object within the game world that can be collected by a player or, occasionally, a non-player character.",
    )
    containsSeason: Optional[
        Union[List[Union["CreativeWorkSeason", str]], "CreativeWorkSeason", str]
    ] = Field(
        default=None,
        description="A season that is part of the media series.",
    )
    numberOfSeasons: Optional[
        Union[List[Union[int, "Integer", str]], int, "Integer", str]
    ] = Field(
        default=None,
        description="The number of seasons in this series.",
    )
    directors: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.",
    )
    episodes: Optional[Union[List[Union["Episode", str]], "Episode", str]] = Field(
        default=None,
        description="An episode of a TV/radio series or season.",
    )
    cheatCode: Optional[
        Union[List[Union["CreativeWork", str]], "CreativeWork", str]
    ] = Field(
        default=None,
        description="Cheat codes to the game.",
    )
    quest: Optional[Union[List[Union["Thing", str]], "Thing", str]] = Field(
        default=None,
        description="The task that a player-controlled character, or group of characters may complete in order to gain a reward.",
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
    numberOfPlayers: Optional[
        Union[List[Union["QuantitativeValue", str]], "QuantitativeValue", str]
    ] = Field(
        default=None,
        description="Indicate how many people can play this game (minimum, maximum, or range).",
    )
    actor: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.",
    )
    characterAttribute: Optional[Union[List[Union["Thing", str]], "Thing", str]] = (
        Field(
            default=None,
            description="A piece of data that represents a particular aspect of a fictional character (skill, power, character points, advantage, disadvantage).",
        )
    )
    musicBy: Optional[
        Union[List[Union["Person", "MusicGroup", str]], "Person", "MusicGroup", str]
    ] = Field(
        default=None,
        description="The composer of the soundtrack.",
    )
    seasons: Optional[
        Union[List[Union["CreativeWorkSeason", str]], "CreativeWorkSeason", str]
    ] = Field(
        default=None,
        description="A season in a media series.",
    )
    gameLocation: Optional[
        Union[
            List[Union[AnyUrl, "URL", "Place", "PostalAddress", str]],
            AnyUrl,
            "URL",
            "Place",
            "PostalAddress",
            str,
        ]
    ] = Field(
        default=None,
        description="Real or fictional location of the game (or part of game).",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.VideoObject import VideoObject
    from pydantic2_schemaorg.Episode import Episode
    from pydantic2_schemaorg.Integer import Integer
    from pydantic2_schemaorg.GamePlayMode import GamePlayMode
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.CreativeWorkSeason import CreativeWorkSeason
    from pydantic2_schemaorg.Thing import Thing
    from pydantic2_schemaorg.CreativeWork import CreativeWork
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic2_schemaorg.MusicGroup import MusicGroup
    from pydantic2_schemaorg.Place import Place
    from pydantic2_schemaorg.PostalAddress import PostalAddress
