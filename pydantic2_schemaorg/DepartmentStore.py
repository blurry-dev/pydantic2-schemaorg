from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class DepartmentStore(Store):
    """A department store.

    See: https://schema.org/DepartmentStore
    Model depth: 5
    """

    type_: str = Field(default="DepartmentStore", alias="@type", const=True)
