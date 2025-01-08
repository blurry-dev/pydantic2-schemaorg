from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Audience import Audience


class BusinessAudience(Audience):
    """A set of characteristics belonging to businesses, e.g. who compose an item's target audience.

    See: https://schema.org/BusinessAudience
    Model depth: 4
    """

    type_: str = Field(default="BusinessAudience", alias="@type", const=True)
    numberOfEmployees: Optional[
        Union[List[Union["QuantitativeValue", str]], "QuantitativeValue", str]
    ] = Field(
        default=None,
        description="The number of employees in an organization, e.g. business.",
    )
    yearlyRevenue: Optional[
        Union[List[Union["QuantitativeValue", str]], "QuantitativeValue", str]
    ] = Field(
        default=None,
        description="The size of the business in annual revenue.",
    )
    yearsInOperation: Optional[
        Union[List[Union["QuantitativeValue", str]], "QuantitativeValue", str]
    ] = Field(
        default=None,
        description="The age of the business.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.QuantitativeValue import QuantitativeValue
