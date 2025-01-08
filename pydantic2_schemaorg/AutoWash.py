from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoWash(AutomotiveBusiness):
    """A car wash business.

    See: https://schema.org/AutoWash
    Model depth: 5
    """

    type_: str = Field(default="AutoWash", alias="@type", const=True)
