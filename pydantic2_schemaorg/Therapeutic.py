from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalDevicePurpose import MedicalDevicePurpose


class Therapeutic(MedicalDevicePurpose):
    """A medical device used for therapeutic purposes.

    See: https://schema.org/Therapeutic
    Model depth: 6
    """

    type_: str = Field(default="Therapeutic", alias="@type", const=True)
