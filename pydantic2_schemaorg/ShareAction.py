from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CommunicateAction import CommunicateAction


class ShareAction(CommunicateAction):
    """The act of distributing content to people for their amusement or edification.

    See: https://schema.org/ShareAction
    Model depth: 5
    """

    type_: str = Field(default="ShareAction", alias="@type", const=True)
