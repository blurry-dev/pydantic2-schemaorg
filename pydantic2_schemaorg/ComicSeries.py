from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Periodical import Periodical


class ComicSeries(Periodical):
    """A sequential publication of comic stories under a unifying title, for example \"The Amazing Spider-Man\"
     or \"Groo the Wanderer\".

    See: https://schema.org/ComicSeries
    Model depth: 5
    """

    type_: str = Field(default="ComicSeries", alias="@type", const=True)
