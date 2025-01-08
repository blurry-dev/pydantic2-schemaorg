from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class AdultEntertainment(EntertainmentBusiness):
    """An adult entertainment establishment.

    See: https://schema.org/AdultEntertainment
    Model depth: 5
    """

    type_: str = Field(default="AdultEntertainment", alias="@type", const=True)
