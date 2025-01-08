from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class RecyclingCenter(LocalBusiness):
    """A recycling center.

    See: https://schema.org/RecyclingCenter
    Model depth: 4
    """

    type_: str = Field(default="RecyclingCenter", alias="@type", const=True)
