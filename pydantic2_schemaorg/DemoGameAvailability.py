from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GameAvailabilityEnumeration import GameAvailabilityEnumeration


class DemoGameAvailability(GameAvailabilityEnumeration):
    """Indicates demo game availability, i.e. a somehow limited demonstration of the full game.

    See: https://schema.org/DemoGameAvailability
    Model depth: 5
    """

    type_: str = Field(default="DemoGameAvailability", alias="@type", const=True)
