from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class MovieRentalStore(Store):
    """A movie rental store.

    See: https://schema.org/MovieRentalStore
    Model depth: 5
    """

    type_: str = Field(default="MovieRentalStore", alias="@type", const=True)
