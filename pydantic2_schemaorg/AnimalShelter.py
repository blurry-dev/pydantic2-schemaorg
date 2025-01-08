from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class AnimalShelter(LocalBusiness):
    """Animal shelter.

    See: https://schema.org/AnimalShelter
    Model depth: 4
    """

    type_: str = Field(default="AnimalShelter", alias="@type", const=True)
