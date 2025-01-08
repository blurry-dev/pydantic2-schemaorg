from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Class import Class


class DataType(Class):
    """The basic data types such as Integers, Strings, etc.

    See: https://schema.org/DataType
    Model depth: 4
    """

    type_: str = Field(default="DataType", alias="@type", const=True)
