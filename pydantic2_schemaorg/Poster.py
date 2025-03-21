from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class Poster(CreativeWork):
    """A large, usually printed placard, bill, or announcement, often illustrated, that is posted to advertise
     or publicize something.

    See: https://schema.org/Poster
    Model depth: 3
    """

    type_: str = Field(default="Poster", alias="@type", const=True)
