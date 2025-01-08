from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EducationalOrganization import EducationalOrganization


class MiddleSchool(EducationalOrganization):
    """A middle school (typically for children aged around 11-14, although this varies somewhat).

    See: https://schema.org/MiddleSchool
    Model depth: 4
    """

    type_: str = Field(default="MiddleSchool", alias="@type", const=True)
