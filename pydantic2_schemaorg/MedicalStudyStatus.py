from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalStudyStatus(MedicalEnumeration):
    """The status of a medical study. Enumerated type.

    See: https://schema.org/MedicalStudyStatus
    Model depth: 5
    """

    type_: str = Field(default="MedicalStudyStatus", alias="@type", const=True)
