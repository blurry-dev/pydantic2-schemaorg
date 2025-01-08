from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class Atlas(CreativeWork):
    """A collection or bound volume of maps, charts, plates or tables, physical or in media form illustrating any
     subject.

    See: https://schema.org/Atlas
    Model depth: 3
    """

    type_: str = Field(default="Atlas", alias="@type", const=True)
