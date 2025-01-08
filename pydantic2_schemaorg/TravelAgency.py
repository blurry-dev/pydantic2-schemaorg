from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class TravelAgency(LocalBusiness):
    """A travel agency.

    See: https://schema.org/TravelAgency
    Model depth: 4
    """

    type_: str = Field(default="TravelAgency", alias="@type", const=True)
