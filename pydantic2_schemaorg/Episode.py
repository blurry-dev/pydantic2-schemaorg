from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class Episode(CreativeWork):
    """A media episode (e.g. TV, radio, video game) which can be part of a series or season.

    See: https://schema.org/Episode
    Model depth: 3
    """

    type_: str = Field(default="Episode", alias="@type", const=True)
    trailer: Optional[Union[List[Union["VideoObject", str]], "VideoObject", str]] = (
        Field(
            default=None,
            description="The trailer of a movie or TV/radio series, season, episode, etc.",
        )
    )
    duration: Optional[Union[List[Union["Duration", str]], "Duration", str]] = Field(
        default=None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
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
    directors: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.",
    )
    partOfSeason: Optional[
        Union[List[Union["CreativeWorkSeason", str]], "CreativeWorkSeason", str]
    ] = Field(
        default=None,
        description="The season to which this episode belongs.",
    )
    actor: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.",
    )
    episodeNumber: Optional[
        Union[List[Union[int, "Integer", str, "Text"]], int, "Integer", str, "Text"]
    ] = Field(
        default=None,
        description="Position of the episode within an ordered group of episodes.",
    )
    partOfSeries: Optional[
        Union[List[Union["CreativeWorkSeries", str]], "CreativeWorkSeries", str]
    ] = Field(
        default=None,
        description="The series to which this episode or season belongs.",
    )
    musicBy: Optional[
        Union[List[Union["Person", "MusicGroup", str]], "Person", "MusicGroup", str]
    ] = Field(
        default=None,
        description="The composer of the soundtrack.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.VideoObject import VideoObject
    from pydantic2_schemaorg.Duration import Duration
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.CreativeWorkSeason import CreativeWorkSeason
    from pydantic2_schemaorg.Integer import Integer
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.CreativeWorkSeries import CreativeWorkSeries
    from pydantic2_schemaorg.MusicGroup import MusicGroup
