from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.FindAction import FindAction


class TrackAction(FindAction):
    """An agent tracks an object for updates. Related actions: * [[FollowAction]]: Unlike FollowAction, TrackAction
     refers to the interest on the location of innanimates objects. * [[SubscribeAction]]: Unlike SubscribeAction,
     TrackAction refers to the interest on the location of innanimate objects.

    See: https://schema.org/TrackAction
    Model depth: 4
    """

    type_: str = Field(default="TrackAction", alias="@type", const=True)
    deliveryMethod: Optional[
        Union[List[Union["DeliveryMethod", str]], "DeliveryMethod", str]
    ] = Field(
        default=None,
        description="A sub property of instrument. The method of delivery.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.DeliveryMethod import DeliveryMethod
