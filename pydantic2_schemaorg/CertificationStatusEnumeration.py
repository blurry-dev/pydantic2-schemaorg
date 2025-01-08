from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class CertificationStatusEnumeration(Enumeration):
    """Enumerates the different statuses of a Certification (Active and Inactive).

    See: https://schema.org/CertificationStatusEnumeration
    Model depth: 4
    """

    type_: str = Field(
        default="CertificationStatusEnumeration", alias="@type", const=True
    )
