from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.OrganizeAction import OrganizeAction


class AllocateAction(OrganizeAction):
    """The act of organizing tasks/objects/events by associating resources to it.

    See: https://schema.org/AllocateAction
    Model depth: 4
    """

    type_: str = Field(default="AllocateAction", alias="@type", const=True)
