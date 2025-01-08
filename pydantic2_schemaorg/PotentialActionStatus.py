from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ActionStatusType import ActionStatusType


class PotentialActionStatus(ActionStatusType):
    """A description of an action that is supported.

    See: https://schema.org/PotentialActionStatus
    Model depth: 6
    """

    type_: str = Field(default="PotentialActionStatus", alias="@type", const=True)
