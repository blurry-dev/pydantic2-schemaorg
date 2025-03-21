from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWorkSeason import CreativeWorkSeason


class RadioSeason(CreativeWorkSeason):
    """Season dedicated to radio broadcast and associated online delivery.

    See: https://schema.org/RadioSeason
    Model depth: 4
    """

    type_: str = Field(default="RadioSeason", alias="@type", const=True)
