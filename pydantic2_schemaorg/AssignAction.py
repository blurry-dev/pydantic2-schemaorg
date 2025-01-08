from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AllocateAction import AllocateAction


class AssignAction(AllocateAction):
    """The act of allocating an action/event/task to some destination (someone or something).

    See: https://schema.org/AssignAction
    Model depth: 5
    """

    type_: str = Field(default="AssignAction", alias="@type", const=True)
