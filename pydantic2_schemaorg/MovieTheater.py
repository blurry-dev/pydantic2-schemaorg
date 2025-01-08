from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic.v1 import StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.EntertainmentBusiness import EntertainmentBusiness
from pydantic2_schemaorg.CivicStructure import CivicStructure


class MovieTheater(EntertainmentBusiness, CivicStructure):
    """A movie theater.

    See: https://schema.org/MovieTheater
    Model depth: 4
    """

    type_: str = Field(default="MovieTheater", alias="@type", const=True)
    screenCount: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", str]],
            StrictInt,
            StrictFloat,
            "Number",
            str,
        ]
    ] = Field(
        default=None,
        description="The number of screens in the movie theater.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Number import Number
