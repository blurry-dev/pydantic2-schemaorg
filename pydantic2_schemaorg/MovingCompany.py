from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class MovingCompany(HomeAndConstructionBusiness):
    """A moving company.

    See: https://schema.org/MovingCompany
    Model depth: 5
    """

    type_: str = Field(default="MovingCompany", alias="@type", const=True)
