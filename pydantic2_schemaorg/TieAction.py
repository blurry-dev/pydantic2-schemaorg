from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AchieveAction import AchieveAction


class TieAction(AchieveAction):
    """The act of reaching a draw in a competitive activity.

    See: https://schema.org/TieAction
    Model depth: 4
    """

    type_: str = Field(default="TieAction", alias="@type", const=True)
