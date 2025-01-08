from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.ConsumeAction import ConsumeAction


class PlayGameAction(ConsumeAction):
    """The act of playing a video game.

    See: https://schema.org/PlayGameAction
    Model depth: 4
    """

    type_: str = Field(default="PlayGameAction", alias="@type", const=True)
    gameAvailabilityType: Optional[
        Union[
            List[Union[str, "Text", "GameAvailabilityEnumeration"]],
            str,
            "Text",
            "GameAvailabilityEnumeration",
        ]
    ] = Field(
        default=None,
        description="Indicates the availability type of the game content associated with this action, such as whether it is a full version or a demo.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.GameAvailabilityEnumeration import (
        GameAvailabilityEnumeration,
    )
