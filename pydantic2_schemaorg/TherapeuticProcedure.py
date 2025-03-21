from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalProcedure import MedicalProcedure


class TherapeuticProcedure(MedicalProcedure):
    """A medical procedure intended primarily for therapeutic purposes, aimed at improving a health condition.

    See: https://schema.org/TherapeuticProcedure
    Model depth: 4
    """

    type_: str = Field(default="TherapeuticProcedure", alias="@type", const=True)
    doseSchedule: Optional[
        Union[List[Union["DoseSchedule", str]], "DoseSchedule", str]
    ] = Field(
        default=None,
        description="A dosing schedule for the drug for a given population, either observed, recommended, or maximum dose based on the type used.",
    )
    adverseOutcome: Optional[
        Union[List[Union["MedicalEntity", str]], "MedicalEntity", str]
    ] = Field(
        default=None,
        description="A possible complication and/or side effect of this therapy. If it is known that an adverse outcome is serious (resulting in death, disability, or permanent damage; requiring hospitalization; or otherwise life-threatening or requiring immediate medical attention), tag it as a seriousAdverseOutcome instead.",
    )
    drug: Optional[Union[List[Union["Drug", str]], "Drug", str]] = Field(
        default=None,
        description="Specifying a drug or medicine used in a medication procedure.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.DoseSchedule import DoseSchedule
    from pydantic2_schemaorg.MedicalEntity import MedicalEntity
    from pydantic2_schemaorg.Drug import Drug
