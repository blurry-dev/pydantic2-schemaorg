from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class RadioStation(LocalBusiness):
    """A radio station.

    See: https://schema.org/RadioStation
    Model depth: 4
    """

    type_: str = Field(default="RadioStation", alias="@type", const=True)
