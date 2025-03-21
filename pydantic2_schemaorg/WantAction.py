from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ReactAction import ReactAction


class WantAction(ReactAction):
    """The act of expressing a desire about the object. An agent wants an object.

    See: https://schema.org/WantAction
    Model depth: 5
    """

    type_: str = Field(default="WantAction", alias="@type", const=True)
