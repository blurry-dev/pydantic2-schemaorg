from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class EntertainmentBusiness(LocalBusiness):
    """A business providing entertainment.

    See: https://schema.org/EntertainmentBusiness
    Model depth: 4
    """

    type_: str = Field(default="EntertainmentBusiness", alias="@type", const=True)
