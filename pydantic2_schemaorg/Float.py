from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Number import Number


class Float(Number):
    """Data type: Floating number.

    See: https://schema.org/Float
    Model depth: 6
    """

    type_: str = Field(default="Float", alias="@type", const=True)
