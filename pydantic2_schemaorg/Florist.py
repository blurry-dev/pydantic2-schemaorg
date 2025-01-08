from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class Florist(Store):
    """A florist.

    See: https://schema.org/Florist
    Model depth: 5
    """

    type_: str = Field(default="Florist", alias="@type", const=True)
