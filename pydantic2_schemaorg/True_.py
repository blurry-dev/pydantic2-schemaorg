from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Boolean import Boolean


class True_(Boolean):
    """The boolean value true.

    See: https://schema.org/True
    Model depth: 6
    """

    type_: str = Field(default="True", alias="@type", const=True)
