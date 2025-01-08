from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.UpdateAction import UpdateAction


class AddAction(UpdateAction):
    """The act of editing by adding an object to a collection.

    See: https://schema.org/AddAction
    Model depth: 4
    """

    type_: str = Field(default="AddAction", alias="@type", const=True)
