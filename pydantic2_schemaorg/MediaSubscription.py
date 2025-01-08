from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class MediaSubscription(Intangible):
    """A subscription which allows a user to access media including audio, video, books, etc.

    See: https://schema.org/MediaSubscription
    Model depth: 3
    """

    type_: str = Field(default="MediaSubscription", alias="@type", const=True)
    authenticator: Optional[
        Union[List[Union["Organization", str]], "Organization", str]
    ] = Field(
        default=None,
        description="The Organization responsible for authenticating the user's subscription. For example, many media apps require a cable/satellite provider to authenticate your subscription before playing media.",
    )
    expectsAcceptanceOf: Optional[Union[List[Union["Offer", str]], "Offer", str]] = (
        Field(
            default=None,
            description="An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.",
        )
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.Offer import Offer
