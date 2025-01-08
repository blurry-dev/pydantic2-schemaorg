from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class Casino(EntertainmentBusiness):
    """A casino.

    See: https://schema.org/Casino
    Model depth: 5
    """

    type_: str = Field(default="Casino", alias="@type", const=True)
