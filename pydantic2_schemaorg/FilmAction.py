from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CreateAction import CreateAction


class FilmAction(CreateAction):
    """The act of capturing sound and moving images on film, video, or digitally.

    See: https://schema.org/FilmAction
    Model depth: 4
    """

    type_: str = Field(default="FilmAction", alias="@type", const=True)
