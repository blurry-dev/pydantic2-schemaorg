from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ConsumeAction import ConsumeAction


class DrinkAction(ConsumeAction):
    """The act of swallowing liquids.

    See: https://schema.org/DrinkAction
    Model depth: 4
    """

    type_: str = Field(default="DrinkAction", alias="@type", const=True)
