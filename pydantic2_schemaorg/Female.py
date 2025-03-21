from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GenderType import GenderType


class Female(GenderType):
    """The female gender.

    See: https://schema.org/Female
    Model depth: 5
    """

    type_: str = Field(default="Female", alias="@type", const=True)
