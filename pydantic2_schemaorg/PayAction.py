from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.TradeAction import TradeAction


class PayAction(TradeAction):
    """An agent pays a price to a participant.

    See: https://schema.org/PayAction
    Model depth: 4
    """

    type_: str = Field(default="PayAction", alias="@type", const=True)
    recipient: Optional[
        Union[
            List[Union["Organization", "Audience", "Person", "ContactPoint", str]],
            "Organization",
            "Audience",
            "Person",
            "ContactPoint",
            str,
        ]
    ] = Field(
        default=None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.Audience import Audience
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.ContactPoint import ContactPoint
