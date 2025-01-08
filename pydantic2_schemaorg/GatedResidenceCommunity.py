from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Residence import Residence


class GatedResidenceCommunity(Residence):
    """Residence type: Gated community.

    See: https://schema.org/GatedResidenceCommunity
    Model depth: 4
    """

    type_: str = Field(default="GatedResidenceCommunity", alias="@type", const=True)
