from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MoveAction import MoveAction


class DepartAction(MoveAction):
    """The act of departing from a place. An agent departs from a fromLocation for a destination, optionally with
     participants.

    See: https://schema.org/DepartAction
    Model depth: 4
    """

    type_: str = Field(default="DepartAction", alias="@type", const=True)
