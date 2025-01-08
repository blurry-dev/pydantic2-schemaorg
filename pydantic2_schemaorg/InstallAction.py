from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ConsumeAction import ConsumeAction


class InstallAction(ConsumeAction):
    """The act of installing an application.

    See: https://schema.org/InstallAction
    Model depth: 4
    """

    type_: str = Field(default="InstallAction", alias="@type", const=True)
