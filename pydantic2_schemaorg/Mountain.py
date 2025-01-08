from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Landform import Landform


class Mountain(Landform):
    """A mountain, like Mount Whitney or Mount Everest.

    See: https://schema.org/Mountain
    Model depth: 4
    """

    type_: str = Field(default="Mountain", alias="@type", const=True)
