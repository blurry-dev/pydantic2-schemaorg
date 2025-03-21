from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Episode import Episode


class RadioEpisode(Episode):
    """A radio episode which can be part of a series or season.

    See: https://schema.org/RadioEpisode
    Model depth: 4
    """

    type_: str = Field(default="RadioEpisode", alias="@type", const=True)
