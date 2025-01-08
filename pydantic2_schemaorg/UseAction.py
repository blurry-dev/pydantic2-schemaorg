from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ConsumeAction import ConsumeAction


class UseAction(ConsumeAction):
    """The act of applying an object to its intended purpose.

    See: https://schema.org/UseAction
    Model depth: 4
    """

    type_: str = Field(default="UseAction", alias="@type", const=True)
