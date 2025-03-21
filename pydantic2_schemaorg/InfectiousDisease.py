from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalCondition import MedicalCondition


class InfectiousDisease(MedicalCondition):
    """An infectious disease is a clinically evident human disease resulting from the presence of pathogenic microbial
     agents, like pathogenic viruses, pathogenic bacteria, fungi, protozoa, multicellular parasites, and
     prions. To be considered an infectious disease, such pathogens are known to be able to cause this disease.

    See: https://schema.org/InfectiousDisease
    Model depth: 4
    """

    type_: str = Field(default="InfectiousDisease", alias="@type", const=True)
    transmissionMethod: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="How the disease spreads, either as a route or vector, for example 'direct contact', 'Aedes aegypti', etc.",
    )
    infectiousAgent: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The actual infectious agent, such as a specific bacterium.",
    )
    infectiousAgentClass: Optional[
        Union[List[Union["InfectiousAgentClass", str]], "InfectiousAgentClass", str]
    ] = Field(
        default=None,
        description="The class of infectious agent (bacteria, prion, etc.) that causes the disease.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.InfectiousAgentClass import InfectiousAgentClass
