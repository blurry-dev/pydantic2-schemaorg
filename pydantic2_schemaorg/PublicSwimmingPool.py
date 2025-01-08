from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.SportsActivityLocation import SportsActivityLocation


class PublicSwimmingPool(SportsActivityLocation):
    """A public swimming pool.

    See: https://schema.org/PublicSwimmingPool
    Model depth: 5
    """

    type_: str = Field(default="PublicSwimmingPool", alias="@type", const=True)
