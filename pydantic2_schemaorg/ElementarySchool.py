from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EducationalOrganization import EducationalOrganization


class ElementarySchool(EducationalOrganization):
    """An elementary school.

    See: https://schema.org/ElementarySchool
    Model depth: 4
    """

    type_: str = Field(default="ElementarySchool", alias="@type", const=True)
