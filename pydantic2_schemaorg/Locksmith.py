from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class Locksmith(HomeAndConstructionBusiness):
    """A locksmith.

    See: https://schema.org/Locksmith
    Model depth: 5
    """

    type_: str = Field(default="Locksmith", alias="@type", const=True)
