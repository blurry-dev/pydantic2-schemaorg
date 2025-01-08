from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class EmploymentAgency(LocalBusiness):
    """An employment agency.

    See: https://schema.org/EmploymentAgency
    Model depth: 4
    """

    type_: str = Field(default="EmploymentAgency", alias="@type", const=True)
