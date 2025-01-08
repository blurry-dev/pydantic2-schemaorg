from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ActionStatusType import ActionStatusType


class CompletedActionStatus(ActionStatusType):
    """An action that has already taken place.

    See: https://schema.org/CompletedActionStatus
    Model depth: 6
    """

    type_: str = Field(default="CompletedActionStatus", alias="@type", const=True)
