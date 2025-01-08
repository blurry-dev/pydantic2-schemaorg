from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.StatusEnumeration import StatusEnumeration


class ActionStatusType(StatusEnumeration):
    """The status of an Action.

    See: https://schema.org/ActionStatusType
    Model depth: 5
    """

    type_: str = Field(default="ActionStatusType", alias="@type", const=True)
