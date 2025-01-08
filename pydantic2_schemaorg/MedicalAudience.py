from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PeopleAudience import PeopleAudience
from pydantic2_schemaorg.Audience import Audience


class MedicalAudience(PeopleAudience, Audience):
    """Target audiences for medical web pages.

    See: https://schema.org/MedicalAudience
    Model depth: 4
    """

    type_: str = Field(default="MedicalAudience", alias="@type", const=True)
