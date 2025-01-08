from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Organization import Organization


class LibrarySystem(Organization):
    """A [[LibrarySystem]] is a collaborative system amongst several libraries.

    See: https://schema.org/LibrarySystem
    Model depth: 3
    """

    type_: str = Field(default="LibrarySystem", alias="@type", const=True)
