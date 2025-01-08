from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ReactAction import ReactAction


class AgreeAction(ReactAction):
    """The act of expressing a consistency of opinion with the object. An agent agrees to/about an object (a proposition,
     topic or theme) with participants.

    See: https://schema.org/AgreeAction
    Model depth: 5
    """

    type_: str = Field(default="AgreeAction", alias="@type", const=True)
