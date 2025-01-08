from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DigitalDocument import DigitalDocument


class PresentationDigitalDocument(DigitalDocument):
    """A file containing slides or used for a presentation.

    See: https://schema.org/PresentationDigitalDocument
    Model depth: 4
    """

    type_: str = Field(default="PresentationDigitalDocument", alias="@type", const=True)
