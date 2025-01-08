from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Organization import Organization


class Consortium(Organization):
    """A Consortium is a membership [[Organization]] whose members are typically Organizations.

    See: https://schema.org/Consortium
    Model depth: 3
    """

    type_: str = Field(default="Consortium", alias="@type", const=True)
