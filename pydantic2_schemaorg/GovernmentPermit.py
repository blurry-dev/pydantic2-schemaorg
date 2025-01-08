from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Permit import Permit


class GovernmentPermit(Permit):
    """A permit issued by a government agency.

    See: https://schema.org/GovernmentPermit
    Model depth: 4
    """

    type_: str = Field(default="GovernmentPermit", alias="@type", const=True)
