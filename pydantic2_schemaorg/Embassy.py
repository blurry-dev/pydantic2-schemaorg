from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GovernmentBuilding import GovernmentBuilding


class Embassy(GovernmentBuilding):
    """An embassy.

    See: https://schema.org/Embassy
    Model depth: 5
    """

    type_: str = Field(default="Embassy", alias="@type", const=True)
