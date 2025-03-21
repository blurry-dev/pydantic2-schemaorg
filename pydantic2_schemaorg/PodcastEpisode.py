from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Episode import Episode


class PodcastEpisode(Episode):
    """A single episode of a podcast series.

    See: https://schema.org/PodcastEpisode
    Model depth: 4
    """

    type_: str = Field(default="PodcastEpisode", alias="@type", const=True)
