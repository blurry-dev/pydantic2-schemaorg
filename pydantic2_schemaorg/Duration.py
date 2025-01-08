from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Quantity import Quantity


class Duration(Quantity):
    """Quantity: Duration (use [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601)).

    See: https://schema.org/Duration
    Model depth: 4
    """

    type_: str = Field(default="Duration", alias="@type", const=True)
