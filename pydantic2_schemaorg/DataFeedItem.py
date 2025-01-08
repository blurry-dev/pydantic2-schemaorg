from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import date, datetime


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class DataFeedItem(Intangible):
    """A single item within a larger data feed.

    See: https://schema.org/DataFeedItem
    Model depth: 3
    """

    type_: str = Field(default="DataFeedItem", alias="@type", const=True)
    item: Optional[Union[List[Union["Thing", str]], "Thing", str]] = Field(
        default=None,
        description="An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists').",
    )
    dateCreated: Optional[
        Union[
            List[Union[datetime, "DateTime", date, "Date", str]],
            datetime,
            "DateTime",
            date,
            "Date",
            str,
        ]
    ] = Field(
        default=None,
        description="The date on which the CreativeWork was created or the item was added to a DataFeed.",
    )
    dateModified: Optional[
        Union[
            List[Union[datetime, "DateTime", date, "Date", str]],
            datetime,
            "DateTime",
            date,
            "Date",
            str,
        ]
    ] = Field(
        default=None,
        description="The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed.",
    )
    dateDeleted: Optional[
        Union[
            List[Union[datetime, "DateTime", date, "Date", str]],
            datetime,
            "DateTime",
            date,
            "Date",
            str,
        ]
    ] = Field(
        default=None,
        description="The datetime the item was removed from the DataFeed.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Thing import Thing
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Date import Date
