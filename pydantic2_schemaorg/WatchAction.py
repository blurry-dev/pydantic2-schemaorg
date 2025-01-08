from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ConsumeAction import ConsumeAction


class WatchAction(ConsumeAction):
    """The act of consuming dynamic/moving visual content.

    See: https://schema.org/WatchAction
    Model depth: 4
    """

    type_: str = Field(default="WatchAction", alias="@type", const=True)
