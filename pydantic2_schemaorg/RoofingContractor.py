from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class RoofingContractor(HomeAndConstructionBusiness):
    """A roofing contractor.

    See: https://schema.org/RoofingContractor
    Model depth: 5
    """

    type_: str = Field(default="RoofingContractor", alias="@type", const=True)
