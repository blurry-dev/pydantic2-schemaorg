from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EducationalOrganization import EducationalOrganization


class CollegeOrUniversity(EducationalOrganization):
    """A college, university, or other third-level educational institution.

    See: https://schema.org/CollegeOrUniversity
    Model depth: 4
    """

    type_: str = Field(default="CollegeOrUniversity", alias="@type", const=True)
