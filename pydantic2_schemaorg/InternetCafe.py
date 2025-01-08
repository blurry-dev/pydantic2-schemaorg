from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class InternetCafe(LocalBusiness):
    """An internet cafe.

    See: https://schema.org/InternetCafe
    Model depth: 4
    """

    type_: str = Field(default="InternetCafe", alias="@type", const=True)
