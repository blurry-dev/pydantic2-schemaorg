from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Action import Action


class InteractAction(Action):
    """The act of interacting with another person or organization.

    See: https://schema.org/InteractAction
    Model depth: 3
    """

    type_: str = Field(default="InteractAction", alias="@type", const=True)
