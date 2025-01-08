from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class TouristInformationCenter(LocalBusiness):
    """A tourist information center.

    See: https://schema.org/TouristInformationCenter
    Model depth: 4
    """

    type_: str = Field(default="TouristInformationCenter", alias="@type", const=True)
