from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LegalForceStatus import LegalForceStatus


class PartiallyInForce(LegalForceStatus):
    """Indicates that parts of the legislation are in force, and parts are not.

    See: https://schema.org/PartiallyInForce
    Model depth: 6
    """

    type_: str = Field(default="PartiallyInForce", alias="@type", const=True)
