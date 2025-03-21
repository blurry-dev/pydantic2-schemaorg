from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalDevicePurpose import MedicalDevicePurpose


class Diagnostic(MedicalDevicePurpose):
    """A medical device used for diagnostic purposes.

    See: https://schema.org/Diagnostic
    Model depth: 6
    """

    type_: str = Field(default="Diagnostic", alias="@type", const=True)
