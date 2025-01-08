from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class AutomotiveBusiness(LocalBusiness):
    """Car repair, sales, or parts.

    See: https://schema.org/AutomotiveBusiness
    Model depth: 4
    """

    type_: str = Field(default="AutomotiveBusiness", alias="@type", const=True)
