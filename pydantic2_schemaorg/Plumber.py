from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class Plumber(HomeAndConstructionBusiness):
    """A plumbing service.

    See: https://schema.org/Plumber
    Model depth: 5
    """

    type_: str = Field(default="Plumber", alias="@type", const=True)
