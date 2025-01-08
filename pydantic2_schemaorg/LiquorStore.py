from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class LiquorStore(Store):
    """A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits.

    See: https://schema.org/LiquorStore
    Model depth: 5
    """

    type_: str = Field(default="LiquorStore", alias="@type", const=True)
