from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoDealer(AutomotiveBusiness):
    """An car dealership.

    See: https://schema.org/AutoDealer
    Model depth: 5
    """

    type_: str = Field(default="AutoDealer", alias="@type", const=True)
