from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class EventVenue(CivicStructure):
    """An event venue.

    See: https://schema.org/EventVenue
    Model depth: 4
    """

    type_: str = Field(default="EventVenue", alias="@type", const=True)
