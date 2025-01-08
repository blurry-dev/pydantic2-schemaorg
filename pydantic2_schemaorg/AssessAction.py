from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Action import Action


class AssessAction(Action):
    """The act of forming one's opinion, reaction or sentiment.

    See: https://schema.org/AssessAction
    Model depth: 3
    """

    type_: str = Field(default="AssessAction", alias="@type", const=True)
