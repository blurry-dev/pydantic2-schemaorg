from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CertificationStatusEnumeration import (
    CertificationStatusEnumeration,
)


class CertificationInactive(CertificationStatusEnumeration):
    """Specifies that a certification is inactive (no longer in effect).

    See: https://schema.org/CertificationInactive
    Model depth: 5
    """

    type_: str = Field(default="CertificationInactive", alias="@type", const=True)
