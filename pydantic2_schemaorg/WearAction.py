from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.UseAction import UseAction


class WearAction(UseAction):
    """The act of dressing oneself in clothing.

    See: https://schema.org/WearAction
    Model depth: 5
    """

    type_: str = Field(default="WearAction", alias="@type", const=True)
