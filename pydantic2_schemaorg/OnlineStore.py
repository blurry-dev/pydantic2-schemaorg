from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.OnlineBusiness import OnlineBusiness


class OnlineStore(OnlineBusiness):
    """An eCommerce site.

    See: https://schema.org/OnlineStore
    Model depth: 4
    """

    type_: str = Field(default="OnlineStore", alias="@type", const=True)
