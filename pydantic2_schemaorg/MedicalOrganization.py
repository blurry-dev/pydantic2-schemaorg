from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic.v1 import StrictBool
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Organization import Organization


class MedicalOrganization(Organization):
    """A medical organization (physical or not), such as hospital, institution or clinic.

    See: https://schema.org/MedicalOrganization
    Model depth: 3
    """

    type_: str = Field(default="MedicalOrganization", alias="@type", const=True)
    isAcceptingNewPatients: Optional[
        Union[List[Union[StrictBool, "Boolean", str]], StrictBool, "Boolean", str]
    ] = Field(
        default=None,
        description="Whether the provider is accepting new patients.",
    )
    medicalSpecialty: Optional[
        Union[List[Union["MedicalSpecialty", str]], "MedicalSpecialty", str]
    ] = Field(
        default=None,
        description="A medical specialty of the provider.",
    )
    healthPlanNetworkId: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Name or unique ID of network. (Networks are often reused across different insurance plans.)",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Boolean import Boolean
    from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty
    from pydantic2_schemaorg.Text import Text
