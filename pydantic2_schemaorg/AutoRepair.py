from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoRepair(AutomotiveBusiness):
    """Car repair business.

    See: https://schema.org/AutoRepair
    Model depth: 5
    """

    type_: str = Field(default="AutoRepair", alias="@type", const=True)
