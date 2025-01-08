from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class TelevisionStation(LocalBusiness):
    """A television station.

    See: https://schema.org/TelevisionStation
    Model depth: 4
    """

    type_: str = Field(default="TelevisionStation", alias="@type", const=True)
