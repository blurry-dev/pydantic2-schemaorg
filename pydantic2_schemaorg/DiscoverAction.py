from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.FindAction import FindAction


class DiscoverAction(FindAction):
    """The act of discovering/finding an object.

    See: https://schema.org/DiscoverAction
    Model depth: 4
    """

    type_: str = Field(default="DiscoverAction", alias="@type", const=True)
