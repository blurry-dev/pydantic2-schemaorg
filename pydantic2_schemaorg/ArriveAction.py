from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MoveAction import MoveAction


class ArriveAction(MoveAction):
    """The act of arriving at a place. An agent arrives at a destination from a fromLocation, optionally with participants.

    See: https://schema.org/ArriveAction
    Model depth: 4
    """

    type_: str = Field(default="ArriveAction", alias="@type", const=True)
