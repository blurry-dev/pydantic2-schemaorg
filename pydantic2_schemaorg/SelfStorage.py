from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class SelfStorage(LocalBusiness):
    """A self-storage facility.

    See: https://schema.org/SelfStorage
    Model depth: 4
    """

    type_: str = Field(default="SelfStorage", alias="@type", const=True)
