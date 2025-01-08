from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Event import Event


class Festival(Event):
    """Event type: Festival.

    See: https://schema.org/Festival
    Model depth: 3
    """

    type_: str = Field(default="Festival", alias="@type", const=True)
