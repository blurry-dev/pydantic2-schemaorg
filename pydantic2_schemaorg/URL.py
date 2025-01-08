from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Text import Text


class URL(Text):
    """Data type: URL.

    See: https://schema.org/URL
    Model depth: 6
    """

    type_: str = Field(default="URL", alias="@type", const=True)
