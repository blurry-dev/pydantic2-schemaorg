from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DigitalDocument import DigitalDocument


class SpreadsheetDigitalDocument(DigitalDocument):
    """A spreadsheet file.

    See: https://schema.org/SpreadsheetDigitalDocument
    Model depth: 4
    """

    type_: str = Field(default="SpreadsheetDigitalDocument", alias="@type", const=True)
