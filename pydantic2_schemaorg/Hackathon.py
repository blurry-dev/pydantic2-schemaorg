from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Event import Event


class Hackathon(Event):
    """A [hackathon](https://en.wikipedia.org/wiki/Hackathon) event.

    See: https://schema.org/Hackathon
    Model depth: 3
    """

    type_: str = Field(default="Hackathon", alias="@type", const=True)
