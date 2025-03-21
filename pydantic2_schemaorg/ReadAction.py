from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ConsumeAction import ConsumeAction


class ReadAction(ConsumeAction):
    """The act of consuming written content.

    See: https://schema.org/ReadAction
    Model depth: 4
    """

    type_: str = Field(default="ReadAction", alias="@type", const=True)
