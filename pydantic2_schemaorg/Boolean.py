from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DataType import DataType


class Boolean(DataType):
    """Boolean: True or False.

    See: https://schema.org/Boolean
    Model depth: 5
    """

    type_: str = Field(default="Boolean", alias="@type", const=True)
