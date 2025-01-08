from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalAudience import MedicalAudience
from pydantic2_schemaorg.Person import Person


class Patient(MedicalAudience, Person):
    """A patient is any person recipient of health care services.

    See: https://schema.org/Patient
    Model depth: 3
    """

    type_: str = Field(default="Patient", alias="@type", const=True)
    diagnosis: Optional[
        Union[List[Union["MedicalCondition", str]], "MedicalCondition", str]
    ] = Field(
        default=None,
        description="One or more alternative conditions considered in the differential diagnosis process as output of a diagnosis process.",
    )
    healthCondition: Optional[
        Union[List[Union["MedicalCondition", str]], "MedicalCondition", str]
    ] = Field(
        default=None,
        description="Specifying the health condition(s) of a patient, medical study, or other target audience.",
    )
    drug: Optional[Union[List[Union["Drug", str]], "Drug", str]] = Field(
        default=None,
        description="Specifying a drug or medicine used in a medication procedure.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.MedicalCondition import MedicalCondition
    from pydantic2_schemaorg.Drug import Drug
