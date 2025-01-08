from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class SeeDoctorHealthAspect(HealthAspectEnumeration):
    """Information about questions that may be asked, when to see a professional, measures before seeing a doctor
     or content about the first consultation.

    See: https://schema.org/SeeDoctorHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="SeeDoctorHealthAspect", alias="@type", const=True)
