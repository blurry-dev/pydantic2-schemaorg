from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EducationalOrganization import EducationalOrganization


class School(EducationalOrganization):
    """A school.

    See: https://schema.org/School
    Model depth: 4
    """

    type_: str = Field(default="School", alias="@type", const=True)
