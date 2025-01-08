from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Action import Action


class OrganizeAction(Action):
    """The act of manipulating/administering/supervising/controlling one or more objects.

    See: https://schema.org/OrganizeAction
    Model depth: 3
    """

    type_: str = Field(default="OrganizeAction", alias="@type", const=True)
