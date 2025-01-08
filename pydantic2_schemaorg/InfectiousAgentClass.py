from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEnumeration import MedicalEnumeration


class InfectiousAgentClass(MedicalEnumeration):
    """Classes of agents or pathogens that transmit infectious diseases. Enumerated type.

    See: https://schema.org/InfectiousAgentClass
    Model depth: 5
    """

    type_: str = Field(default="InfectiousAgentClass", alias="@type", const=True)
