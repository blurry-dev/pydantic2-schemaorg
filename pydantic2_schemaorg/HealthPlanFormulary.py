from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic.v1 import StrictBool
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class HealthPlanFormulary(Intangible):
    """For a given health insurance plan, the specification for costs and coverage of prescription drugs.

    See: https://schema.org/HealthPlanFormulary
    Model depth: 3
    """

    type_: str = Field(default="HealthPlanFormulary", alias="@type", const=True)
    healthPlanCostSharing: Optional[
        Union[List[Union[StrictBool, "Boolean", str]], StrictBool, "Boolean", str]
    ] = Field(
        default=None,
        description="The costs to the patient for services under this network or formulary.",
    )
    offersPrescriptionByMail: Optional[
        Union[List[Union[StrictBool, "Boolean", str]], StrictBool, "Boolean", str]
    ] = Field(
        default=None,
        description="Whether prescriptions can be delivered by mail.",
    )
    healthPlanDrugTier: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The tier(s) of drugs offered by this formulary or insurance plan.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Boolean import Boolean
    from pydantic2_schemaorg.Text import Text
