from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import StrictInt, StrictFloat


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEntity import MedicalEntity


class DrugCost(MedicalEntity):
    """The cost per unit of a medical drug. Note that this type is not meant to represent the price in an offer of a drug
     for sale; see the Offer type for that. This type will typically be used to tag wholesale or average retail cost
     of a drug, or maximum reimbursable cost. Costs of medical drugs vary widely depending on how and where they
     are paid for, so while this type captures some of the variables, costs should be used with caution by consumers
     of this schema's markup.

    See: https://schema.org/DrugCost
    Model depth: 3
    """

    type_: str = Field(default="DrugCost", alias="@type", const=True)
    drugUnit: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The unit in which the drug is measured, e.g. '5 mg tablet'.",
    )
    applicableLocation: Optional[
        Union[List[Union["AdministrativeArea", str]], "AdministrativeArea", str]
    ] = Field(
        default=None,
        description="The location in which the status applies.",
    )
    costOrigin: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Additional details to capture the origin of the cost data. For example, 'Medicare Part B'.",
    )
    costPerUnit: Optional[
        Union[
            List[
                Union[StrictInt, StrictFloat, "Number", str, "Text", "QualitativeValue"]
            ],
            StrictInt,
            StrictFloat,
            "Number",
            str,
            "Text",
            "QualitativeValue",
        ]
    ] = Field(
        default=None,
        description="The cost per unit of the drug.",
    )
    costCategory: Optional[
        Union[List[Union["DrugCostCategory", str]], "DrugCostCategory", str]
    ] = Field(
        default=None,
        description="The category of cost, such as wholesale, retail, reimbursement cap, etc.",
    )
    costCurrency: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The currency (in 3-letter) of the drug cost. See: http://en.wikipedia.org/wiki/ISO_4217.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.QualitativeValue import QualitativeValue
    from pydantic2_schemaorg.DrugCostCategory import DrugCostCategory
