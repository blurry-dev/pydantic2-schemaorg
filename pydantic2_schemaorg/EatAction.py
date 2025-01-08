from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ConsumeAction import ConsumeAction


class EatAction(ConsumeAction):
    """The act of swallowing solid objects.

    See: https://schema.org/EatAction
    Model depth: 4
    """

    type_: str = Field(default="EatAction", alias="@type", const=True)
