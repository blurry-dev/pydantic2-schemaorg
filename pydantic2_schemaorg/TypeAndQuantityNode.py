from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic.v1 import AnyUrl, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.StructuredValue import StructuredValue


class TypeAndQuantityNode(StructuredValue):
    """A structured value indicating the quantity, unit of measurement, and business function of goods included
     in a bundle offer.

    See: https://schema.org/TypeAndQuantityNode
    Model depth: 4
    """

    type_: str = Field(default="TypeAndQuantityNode", alias="@type", const=True)
    amountOfThisGood: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", str]],
            StrictInt,
            StrictFloat,
            "Number",
            str,
        ]
    ] = Field(
        default=None,
        description="The quantity of the goods included in the offer.",
    )
    unitCode: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description="The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.",
    )
    businessFunction: Optional[
        Union[List[Union["BusinessFunction", str]], "BusinessFunction", str]
    ] = Field(
        default=None,
        description="The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.",
    )
    unitText: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for <a href='unitCode'>unitCode</a>.",
    )
    typeOfGood: Optional[
        Union[List[Union["Service", "Product", str]], "Service", "Product", str]
    ] = Field(
        default=None,
        description="The product that this structured value is referring to.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.BusinessFunction import BusinessFunction
    from pydantic2_schemaorg.Service import Service
    from pydantic2_schemaorg.Product import Product
