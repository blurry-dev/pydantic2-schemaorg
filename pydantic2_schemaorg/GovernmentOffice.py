from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class GovernmentOffice(LocalBusiness):
    """A government office&#x2014;for example, an IRS or DMV office.

    See: https://schema.org/GovernmentOffice
    Model depth: 4
    """

    type_: str = Field(default="GovernmentOffice", alias="@type", const=True)
