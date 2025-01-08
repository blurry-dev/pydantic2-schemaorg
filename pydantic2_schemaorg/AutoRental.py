from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoRental(AutomotiveBusiness):
    """A car rental business.

    See: https://schema.org/AutoRental
    Model depth: 5
    """

    type_: str = Field(default="AutoRental", alias="@type", const=True)
