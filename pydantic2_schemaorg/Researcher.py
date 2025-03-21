from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Audience import Audience


class Researcher(Audience):
    """Researchers.

    See: https://schema.org/Researcher
    Model depth: 4
    """

    type_: str = Field(default="Researcher", alias="@type", const=True)
