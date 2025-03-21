from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LegalForceStatus import LegalForceStatus


class InForce(LegalForceStatus):
    """Indicates that a legislation is in force.

    See: https://schema.org/InForce
    Model depth: 6
    """

    type_: str = Field(default="InForce", alias="@type", const=True)
