from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GovernmentBuilding import GovernmentBuilding


class DefenceEstablishment(GovernmentBuilding):
    """A defence establishment, such as an army or navy base.

    See: https://schema.org/DefenceEstablishment
    Model depth: 5
    """

    type_: str = Field(default="DefenceEstablishment", alias="@type", const=True)
