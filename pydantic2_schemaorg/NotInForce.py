from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LegalForceStatus import LegalForceStatus


class NotInForce(LegalForceStatus):
    """Indicates that a legislation is currently not in force.

    See: https://schema.org/NotInForce
    Model depth: 6
    """

    type_: str = Field(default="NotInForce", alias="@type", const=True)
