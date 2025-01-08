from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class GeneralContractor(HomeAndConstructionBusiness):
    """A general contractor.

    See: https://schema.org/GeneralContractor
    Model depth: 5
    """

    type_: str = Field(default="GeneralContractor", alias="@type", const=True)
