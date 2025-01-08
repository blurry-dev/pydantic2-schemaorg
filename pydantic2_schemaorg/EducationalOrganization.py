from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure
from pydantic2_schemaorg.Organization import Organization


class EducationalOrganization(CivicStructure, Organization):
    """An educational organization.

    See: https://schema.org/EducationalOrganization
    Model depth: 3
    """

    type_: str = Field(default="EducationalOrganization", alias="@type", const=True)
    alumni: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="Alumni of an organization.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Person import Person
