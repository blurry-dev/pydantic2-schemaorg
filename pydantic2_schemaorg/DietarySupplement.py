from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import StrictBool


from pydantic.v1 import Field
from pydantic2_schemaorg.Substance import Substance
from pydantic2_schemaorg.Product import Product


class DietarySupplement(Substance, Product):
    """A product taken by mouth that contains a dietary ingredient intended to supplement the diet. Dietary ingredients
     may include vitamins, minerals, herbs or other botanicals, amino acids, and substances such as enzymes,
     organ tissues, glandulars and metabolites.

    See: https://schema.org/DietarySupplement
    Model depth: 3
    """

    type_: str = Field(default="DietarySupplement", alias="@type", const=True)
    proprietaryName: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Proprietary name given to the diet plan, typically by its originator or creator.",
    )
    recommendedIntake: Optional[
        Union[
            List[Union["RecommendedDoseSchedule", str]], "RecommendedDoseSchedule", str
        ]
    ] = Field(
        default=None,
        description="Recommended intake of this supplement for a given population as defined by a specific recommending authority.",
    )
    safetyConsideration: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Any potential safety concern associated with the supplement. May include interactions with other drugs and foods, pregnancy, breastfeeding, known adverse reactions, and documented efficacy of the supplement.",
    )
    nonProprietaryName: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The generic name of this drug or supplement.",
    )
    maximumIntake: Optional[
        Union[List[Union["MaximumDoseSchedule", str]], "MaximumDoseSchedule", str]
    ] = Field(
        default=None,
        description="Recommended intake of this supplement for a given population as defined by a specific recommending authority.",
    )
    legalStatus: Optional[
        Union[
            List[Union[str, "Text", "DrugLegalStatus", "MedicalEnumeration"]],
            str,
            "Text",
            "DrugLegalStatus",
            "MedicalEnumeration",
        ]
    ] = Field(
        default=None,
        description="The drug or supplement's legal status, including any controlled substance schedules that apply.",
    )
    activeIngredient: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="An active ingredient, typically chemical compounds and/or biologic substances.",
    )
    mechanismOfAction: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The specific biochemical interaction through which this drug or supplement produces its pharmacological effect.",
    )
    isProprietary: Optional[
        Union[List[Union[StrictBool, "Boolean", str]], StrictBool, "Boolean", str]
    ] = Field(
        default=None,
        description="True if this item's name is a proprietary/brand name (vs. generic name).",
    )
    targetPopulation: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Characteristics of the population for which this is intended, or which typically uses it, e.g. 'adults'.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.RecommendedDoseSchedule import RecommendedDoseSchedule
    from pydantic2_schemaorg.MaximumDoseSchedule import MaximumDoseSchedule
    from pydantic2_schemaorg.DrugLegalStatus import DrugLegalStatus
    from pydantic2_schemaorg.MedicalEnumeration import MedicalEnumeration
    from pydantic2_schemaorg.Boolean import Boolean
