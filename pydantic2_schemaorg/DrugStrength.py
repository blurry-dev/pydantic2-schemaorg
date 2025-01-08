from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import StrictInt, StrictFloat


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalIntangible import MedicalIntangible


class DrugStrength(MedicalIntangible):
    """A specific strength in which a medical drug is available in a specific country.

    See: https://schema.org/DrugStrength
    Model depth: 4
    """

    type_: str = Field(default="DrugStrength", alias="@type", const=True)
    strengthUnit: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The units of an active ingredient's strength, e.g. mg.",
    )
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
    strengthValue: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", str]],
            StrictInt,
            StrictFloat,
            "Number",
            str,
        ]
    ] = Field(
        default=None,
        description="The value of an active ingredient's strength, e.g. 325.",
    )
    availableIn: Optional[
        Union[List[Union["AdministrativeArea", str]], "AdministrativeArea", str]
    ] = Field(
        default=None,
        description="The location in which the strength is available.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.MaximumDoseSchedule import MaximumDoseSchedule
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.AdministrativeArea import AdministrativeArea
