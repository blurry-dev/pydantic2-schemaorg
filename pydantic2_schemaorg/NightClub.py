from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class NightClub(EntertainmentBusiness):
    """A nightclub or discotheque.

    See: https://schema.org/NightClub
    Model depth: 5
    """

    type_: str = Field(default="NightClub", alias="@type", const=True)
