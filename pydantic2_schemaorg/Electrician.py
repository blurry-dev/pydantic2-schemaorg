from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class Electrician(HomeAndConstructionBusiness):
    """An electrician.

    See: https://schema.org/Electrician
    Model depth: 5
    """

    type_: str = Field(default="Electrician", alias="@type", const=True)
