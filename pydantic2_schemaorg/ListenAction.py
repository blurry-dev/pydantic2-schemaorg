from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ConsumeAction import ConsumeAction


class ListenAction(ConsumeAction):
    """The act of consuming audio content.

    See: https://schema.org/ListenAction
    Model depth: 4
    """

    type_: str = Field(default="ListenAction", alias="@type", const=True)
