from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class SportsActivityLocation(LocalBusiness):
    """A sports location, such as a playing field.

    See: https://schema.org/SportsActivityLocation
    Model depth: 4
    """

    type_: str = Field(default="SportsActivityLocation", alias="@type", const=True)
