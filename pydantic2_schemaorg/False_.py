from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Boolean import Boolean


class False_(Boolean):
    """The boolean value false.

    See: https://schema.org/False
    Model depth: 6
    """

    type_: str = Field(default="False", alias="@type", const=True)
