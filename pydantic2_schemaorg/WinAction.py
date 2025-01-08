from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.AchieveAction import AchieveAction


class WinAction(AchieveAction):
    """The act of achieving victory in a competitive activity.

    See: https://schema.org/WinAction
    Model depth: 4
    """

    type_: str = Field(default="WinAction", alias="@type", const=True)
    loser: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="A sub property of participant. The loser of the action.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Person import Person
