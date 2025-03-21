from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ActionStatusType import ActionStatusType


class ActiveActionStatus(ActionStatusType):
    """An in-progress action (e.g., while watching the movie, or driving to a location).

    See: https://schema.org/ActiveActionStatus
    Model depth: 6
    """

    type_: str = Field(default="ActiveActionStatus", alias="@type", const=True)
