from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ControlAction import ControlAction


class DeactivateAction(ControlAction):
    """The act of stopping or deactivating a device or application (e.g. stopping a timer or turning off a flashlight).

    See: https://schema.org/DeactivateAction
    Model depth: 4
    """

    type_: str = Field(default="DeactivateAction", alias="@type", const=True)
