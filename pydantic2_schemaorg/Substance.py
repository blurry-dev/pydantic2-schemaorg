from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEntity import MedicalEntity


class Substance(MedicalEntity):
    """Any matter of defined composition that has discrete existence, whose origin may be biological, mineral or
     chemical.

    See: https://schema.org/Substance
    Model depth: 3
    """

    type_: str = Field(default="Substance", alias="@type", const=True)
    maximumIntake: Optional[
        Union[List[Union["MaximumDoseSchedule", str]], "MaximumDoseSchedule", str]
    ] = Field(
        default=None,
        description="Recommended intake of this supplement for a given population as defined by a specific recommending authority.",
    )
    activeIngredient: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="An active ingredient, typically chemical compounds and/or biologic substances.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.MaximumDoseSchedule import MaximumDoseSchedule
    from pydantic2_schemaorg.Text import Text
