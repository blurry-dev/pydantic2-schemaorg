from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CertificationStatusEnumeration import (
    CertificationStatusEnumeration,
)


class CertificationActive(CertificationStatusEnumeration):
    """Specifies that a certification is active.

    See: https://schema.org/CertificationActive
    Model depth: 5
    """

    type_: str = Field(default="CertificationActive", alias="@type", const=True)
