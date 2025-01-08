from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Action import Action


class TransferAction(Action):
    """The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another.

    See: https://schema.org/TransferAction
    Model depth: 3
    """

    type_: str = Field(default="TransferAction", alias="@type", const=True)
    toLocation: Optional[Union[List[Union["Place", str]], "Place", str]] = Field(
        default=None,
        description="A sub property of location. The final location of the object or the agent after the action.",
    )
    fromLocation: Optional[Union[List[Union["Place", str]], "Place", str]] = Field(
        default=None,
        description="A sub property of location. The original location of the object or the agent before the action.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Place import Place
