from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EducationalOrganization import EducationalOrganization


class HighSchool(EducationalOrganization):
    """A high school.

    See: https://schema.org/HighSchool
    Model depth: 4
    """

    type_: str = Field(default="HighSchool", alias="@type", const=True)
