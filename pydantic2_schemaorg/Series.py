from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class Series(Intangible):
    """A Series in schema.org is a group of related items, typically but not necessarily of the same kind. See also
     [[CreativeWorkSeries]], [[EventSeries]].

    See: https://schema.org/Series
    Model depth: 3
    """

    type_: str = Field(default="Series", alias="@type", const=True)
