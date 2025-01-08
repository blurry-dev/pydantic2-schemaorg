from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AllocateAction import AllocateAction


class AcceptAction(AllocateAction):
    """The act of committing to/adopting an object. Related actions: * [[RejectAction]]: The antonym of AcceptAction.

    See: https://schema.org/AcceptAction
    Model depth: 5
    """

    type_: str = Field(default="AcceptAction", alias="@type", const=True)
