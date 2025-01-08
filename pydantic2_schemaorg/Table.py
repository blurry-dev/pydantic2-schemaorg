from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WebPageElement import WebPageElement


class Table(WebPageElement):
    """A table on a Web page.

    See: https://schema.org/Table
    Model depth: 4
    """

    type_: str = Field(default="Table", alias="@type", const=True)
