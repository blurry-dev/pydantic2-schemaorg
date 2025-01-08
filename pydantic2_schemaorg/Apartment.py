from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import StrictInt, StrictFloat


from pydantic.v1 import Field
from pydantic2_schemaorg.Accommodation import Accommodation


class Apartment(Accommodation):
    """An apartment (in American English) or flat (in British English) is a self-contained housing unit (a type of
     residential real estate) that occupies only part of a building (source: Wikipedia, the free encyclopedia,
     see <a href=\"http://en.wikipedia.org/wiki/Apartment\">http://en.wikipedia.org/wiki/Apartment</a>).

    See: https://schema.org/Apartment
    Model depth: 4
    """

    type_: str = Field(default="Apartment", alias="@type", const=True)
    occupancy: Optional[
        Union[List[Union["QuantitativeValue", str]], "QuantitativeValue", str]
    ] = Field(
        default=None,
        description="The allowed total occupancy for the accommodation in persons (including infants etc). For individual accommodations, this is not necessarily the legal maximum but defines the permitted usage as per the contractual agreement (e.g. a double room used by a single person). Typical unit code(s): C62 for person.",
    )
    numberOfRooms: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", "QuantitativeValue", str]],
            StrictInt,
            StrictFloat,
            "Number",
            "QuantitativeValue",
            str,
        ]
    ] = Field(
        default=None,
        description="The number of rooms (excluding bathrooms and closets) of the accommodation or lodging business. Typical unit code(s): ROM for room or C62 for no unit. The type of room can be put in the unitText property of the QuantitativeValue.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic2_schemaorg.Number import Number
