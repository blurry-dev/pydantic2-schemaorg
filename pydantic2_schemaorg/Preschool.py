from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EducationalOrganization import EducationalOrganization


class Preschool(EducationalOrganization):
    """A preschool.

    See: https://schema.org/Preschool
    Model depth: 4
    """

    type_: str = Field(default="Preschool", alias="@type", const=True)
