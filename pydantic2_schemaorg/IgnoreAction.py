from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AssessAction import AssessAction


class IgnoreAction(AssessAction):
    """The act of intentionally disregarding the object. An agent ignores an object.

    See: https://schema.org/IgnoreAction
    Model depth: 4
    """

    type_: str = Field(default="IgnoreAction", alias="@type", const=True)
