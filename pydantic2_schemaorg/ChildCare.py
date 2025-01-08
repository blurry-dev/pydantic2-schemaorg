from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class ChildCare(LocalBusiness):
    """A Childcare center.

    See: https://schema.org/ChildCare
    Model depth: 4
    """

    type_: str = Field(default="ChildCare", alias="@type", const=True)
