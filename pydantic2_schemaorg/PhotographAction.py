from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CreateAction import CreateAction


class PhotographAction(CreateAction):
    """The act of capturing still images of objects using a camera.

    See: https://schema.org/PhotographAction
    Model depth: 4
    """

    type_: str = Field(default="PhotographAction", alias="@type", const=True)
