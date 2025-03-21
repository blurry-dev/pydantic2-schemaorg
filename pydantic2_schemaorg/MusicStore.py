from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class MusicStore(Store):
    """A music store.

    See: https://schema.org/MusicStore
    Model depth: 5
    """

    type_: str = Field(default="MusicStore", alias="@type", const=True)
