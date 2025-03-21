from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.InteractAction import InteractAction


class MarryAction(InteractAction):
    """The act of marrying a person.

    See: https://schema.org/MarryAction
    Model depth: 4
    """

    type_: str = Field(default="MarryAction", alias="@type", const=True)
