from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic.v1 import StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Offer import Offer


class AggregateOffer(Offer):
    """When a single product is associated with multiple offers (for example, the same pair of shoes is offered by
     different merchants), then AggregateOffer can be used. Note: AggregateOffers are normally expected to
     associate multiple offers that all share the same defined [[businessFunction]] value, or default to http://purl.org/goodrelations/v1#Sell
     if businessFunction is not explicitly defined.

    See: https://schema.org/AggregateOffer
    Model depth: 4
    """

    type_: str = Field(default="AggregateOffer", alias="@type", const=True)
    highPrice: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", str, "Text"]],
            StrictInt,
            StrictFloat,
            "Number",
            str,
            "Text",
        ]
    ] = Field(
        default=None,
        description="The highest price of all offers available. Usage guidelines: * Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols. * Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.",
    )
    offerCount: Optional[
        Union[List[Union[int, "Integer", str]], int, "Integer", str]
    ] = Field(
        default=None,
        description="The number of offers for the product.",
    )
    lowPrice: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", str, "Text"]],
            StrictInt,
            StrictFloat,
            "Number",
            str,
            "Text",
        ]
    ] = Field(
        default=None,
        description="The lowest price of all offers available. Usage guidelines: * Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols. * Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.",
    )
    offers: Optional[
        Union[List[Union["Demand", "Offer", str]], "Demand", "Offer", str]
    ] = Field(
        default=None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Integer import Integer
    from pydantic2_schemaorg.Demand import Demand
    from pydantic2_schemaorg.Offer import Offer
