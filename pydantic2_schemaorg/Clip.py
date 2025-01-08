from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import StrictInt, StrictFloat


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class Clip(CreativeWork):
    """A short TV or radio program or a segment/part of a program.

    See: https://schema.org/Clip
    Model depth: 3
    """

    type_: str = Field(default="Clip", alias="@type", const=True)
    actors: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.",
    )
    director: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.",
    )
    endOffset: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", "HyperTocEntry", str]],
            StrictInt,
            StrictFloat,
            "Number",
            "HyperTocEntry",
            str,
        ]
    ] = Field(
        default=None,
        description="The end time of the clip expressed as the number of seconds from the beginning of the work.",
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
    partOfEpisode: Optional[Union[List[Union["Episode", str]], "Episode", str]] = Field(
        default=None,
        description="The episode to which this clip belongs.",
    )
    actor: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.",
    )
    startOffset: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", "HyperTocEntry", str]],
            StrictInt,
            StrictFloat,
            "Number",
            "HyperTocEntry",
            str,
        ]
    ] = Field(
        default=None,
        description="The start time of the clip expressed as the number of seconds from the beginning of the work.",
    )
    partOfSeries: Optional[
        Union[List[Union["CreativeWorkSeries", str]], "CreativeWorkSeries", str]
    ] = Field(
        default=None,
        description="The series to which this episode or season belongs.",
    )
    clipNumber: Optional[
        Union[List[Union[int, "Integer", str, "Text"]], int, "Integer", str, "Text"]
    ] = Field(
        default=None,
        description="Position of the clip within an ordered group of clips.",
    )
    musicBy: Optional[
        Union[List[Union["Person", "MusicGroup", str]], "Person", "MusicGroup", str]
    ] = Field(
        default=None,
        description="The composer of the soundtrack.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.HyperTocEntry import HyperTocEntry
    from pydantic2_schemaorg.CreativeWorkSeason import CreativeWorkSeason
    from pydantic2_schemaorg.Episode import Episode
    from pydantic2_schemaorg.CreativeWorkSeries import CreativeWorkSeries
    from pydantic2_schemaorg.Integer import Integer
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.MusicGroup import MusicGroup
