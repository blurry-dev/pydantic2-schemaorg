from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class NotYetRecruiting(MedicalStudyStatus):
    """Not yet recruiting.

    See: https://schema.org/NotYetRecruiting
    Model depth: 6
    """

    type_: str = Field(default="NotYetRecruiting", alias="@type", const=True)
