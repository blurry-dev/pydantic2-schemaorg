from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Action import Action


class ControlAction(Action):
    """An agent controls a device or application.

    See: https://schema.org/ControlAction
    Model depth: 3
    """

    type_: str = Field(default="ControlAction", alias="@type", const=True)
