from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class RealEstateAgent(LocalBusiness):
    """A real-estate agent.

    See: https://schema.org/RealEstateAgent
    Model depth: 4
    """

    type_: str = Field(default="RealEstateAgent", alias="@type", const=True)
