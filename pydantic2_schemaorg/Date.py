from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DataType import DataType


class Date(DataType):
    """A date value in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).

    See: https://schema.org/Date
    Model depth: 5
    """

    type_: str = Field(default="Date", alias="@type", const=True)
