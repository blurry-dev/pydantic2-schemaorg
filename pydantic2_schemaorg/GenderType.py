from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class GenderType(Enumeration):
    """An enumeration of genders.

    See: https://schema.org/GenderType
    Model depth: 4
    """

    type_: str = Field(default="GenderType", alias="@type", const=True)
