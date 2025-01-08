from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GovernmentBuilding import GovernmentBuilding


class Courthouse(GovernmentBuilding):
    """A courthouse.

    See: https://schema.org/Courthouse
    Model depth: 5
    """

    type_: str = Field(default="Courthouse", alias="@type", const=True)
