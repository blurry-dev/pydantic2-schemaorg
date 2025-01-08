from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.UpdateAction import UpdateAction


class DeleteAction(UpdateAction):
    """The act of editing a recipient by removing one of its objects.

    See: https://schema.org/DeleteAction
    Model depth: 4
    """

    type_: str = Field(default="DeleteAction", alias="@type", const=True)
