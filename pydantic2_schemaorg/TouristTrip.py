from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Trip import Trip


class TouristTrip(Trip):
    """A tourist trip. A created itinerary of visits to one or more places of interest ([[TouristAttraction]]/[[TouristDestination]])
     often linked by a similar theme, geographic area, or interest to a particular [[touristType]]. The [UNWTO](http://www2.unwto.org/)
     defines tourism trip as the Trip taken by visitors. (See examples below.)

    See: https://schema.org/TouristTrip
    Model depth: 4
    """

    type_: str = Field(default="TouristTrip", alias="@type", const=True)
    touristType: Optional[
        Union[List[Union[str, "Text", "Audience"]], str, "Text", "Audience"]
    ] = Field(
        default=None,
        description="Attraction suitable for type(s) of tourist. E.g. children, visitors from a particular country, etc.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Audience import Audience
