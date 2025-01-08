from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ConsumeAction import ConsumeAction


class ViewAction(ConsumeAction):
    """The act of consuming static visual content.

    See: https://schema.org/ViewAction
    Model depth: 4
    """

    type_: str = Field(default="ViewAction", alias="@type", const=True)
