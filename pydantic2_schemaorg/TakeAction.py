from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.TransferAction import TransferAction


class TakeAction(TransferAction):
    """The act of gaining ownership of an object from an origin. Reciprocal of GiveAction. Related actions: * [[GiveAction]]:
     The reciprocal of TakeAction. * [[ReceiveAction]]: Unlike ReceiveAction, TakeAction implies that ownership
     has been transferred.

    See: https://schema.org/TakeAction
    Model depth: 4
    """

    type_: str = Field(default="TakeAction", alias="@type", const=True)
