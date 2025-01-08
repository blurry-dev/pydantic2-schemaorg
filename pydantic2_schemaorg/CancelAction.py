from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PlanAction import PlanAction


class CancelAction(PlanAction):
    """The act of asserting that a future event/action is no longer going to happen. Related actions: * [[ConfirmAction]]:
     The antonym of CancelAction.

    See: https://schema.org/CancelAction
    Model depth: 5
    """

    type_: str = Field(default="CancelAction", alias="@type", const=True)
