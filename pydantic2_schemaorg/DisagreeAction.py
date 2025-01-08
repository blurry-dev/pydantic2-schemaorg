from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ReactAction import ReactAction


class DisagreeAction(ReactAction):
    """The act of expressing a difference of opinion with the object. An agent disagrees to/about an object (a proposition,
     topic or theme) with participants.

    See: https://schema.org/DisagreeAction
    Model depth: 5
    """

    type_: str = Field(default="DisagreeAction", alias="@type", const=True)
