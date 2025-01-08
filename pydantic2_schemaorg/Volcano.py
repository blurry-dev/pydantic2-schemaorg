from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Landform import Landform


class Volcano(Landform):
    """A volcano, like Fujisan.

    See: https://schema.org/Volcano
    Model depth: 4
    """

    type_: str = Field(default="Volcano", alias="@type", const=True)
