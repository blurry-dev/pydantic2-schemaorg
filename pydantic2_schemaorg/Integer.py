from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Number import Number


class Integer(Number):
    """Data type: Integer.

    See: https://schema.org/Integer
    Model depth: 6
    """

    type_: str = Field(default="Integer", alias="@type", const=True)
