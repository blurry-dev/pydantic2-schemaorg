from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class ComedyClub(EntertainmentBusiness):
    """A comedy club.

    See: https://schema.org/ComedyClub
    Model depth: 5
    """

    type_: str = Field(default="ComedyClub", alias="@type", const=True)
