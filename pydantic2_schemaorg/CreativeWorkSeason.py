from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import date, datetime


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class CreativeWorkSeason(CreativeWork):
    """A media season, e.g. TV, radio, video game etc.

    See: https://schema.org/CreativeWorkSeason
    Model depth: 3
    """

    type_: str = Field(default="CreativeWorkSeason", alias="@type", const=True)
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
    endDate: Optional[
        Union[
            List[Union[datetime, "DateTime", date, "Date", str]],
            datetime,
            "DateTime",
            date,
            "Date",
            str,
        ]
    ] = Field(
        default=None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    productionCompany: Optional[
        Union[List[Union["Organization", str]], "Organization", str]
    ] = Field(
        default=None,
        description="The production company or studio responsible for the item, e.g. series, video game, episode etc.",
    )
    director: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.",
    )
    episodes: Optional[Union[List[Union["Episode", str]], "Episode", str]] = Field(
        default=None,
        description="An episode of a TV/radio series or season.",
    )
    actor: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.",
    )
    partOfSeries: Optional[
        Union[List[Union["CreativeWorkSeries", str]], "CreativeWorkSeries", str]
    ] = Field(
        default=None,
        description="The series to which this episode or season belongs.",
    )
    startDate: Optional[
        Union[
            List[Union[datetime, "DateTime", date, "Date", str]],
            datetime,
            "DateTime",
            date,
            "Date",
            str,
        ]
    ] = Field(
        default=None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    seasonNumber: Optional[
        Union[List[Union[int, "Integer", str, "Text"]], int, "Integer", str, "Text"]
    ] = Field(
        default=None,
        description="Position of the season within an ordered group of seasons.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.VideoObject import VideoObject
    from pydantic2_schemaorg.Episode import Episode
    from pydantic2_schemaorg.Integer import Integer
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Date import Date
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.CreativeWorkSeries import CreativeWorkSeries
    from pydantic2_schemaorg.Text import Text
