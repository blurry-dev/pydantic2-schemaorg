from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Trip import Trip


class BoatTrip(Trip):
    """A trip on a commercial ferry line.

    See: https://schema.org/BoatTrip
    Model depth: 4
    """

    type_: str = Field(default="BoatTrip", alias="@type", const=True)
    departureBoatTerminal: Optional[
        Union[List[Union["BoatTerminal", str]], "BoatTerminal", str]
    ] = Field(
        default=None,
        description="The terminal or port from which the boat departs.",
    )
    arrivalBoatTerminal: Optional[
        Union[List[Union["BoatTerminal", str]], "BoatTerminal", str]
    ] = Field(
        default=None,
        description="The terminal or port from which the boat arrives.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.BoatTerminal import BoatTerminal
