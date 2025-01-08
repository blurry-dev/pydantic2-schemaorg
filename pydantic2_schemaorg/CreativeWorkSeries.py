from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import date, datetime


from pydantic.v1 import Field
from pydantic2_schemaorg.Series import Series
from pydantic2_schemaorg.CreativeWork import CreativeWork


class CreativeWorkSeries(Series, CreativeWork):
    """A CreativeWorkSeries in schema.org is a group of related items, typically but not necessarily of the same
     kind. CreativeWorkSeries are usually organized into some order, often chronological. Unlike [[ItemList]]
     which is a general purpose data structure for lists of things, the emphasis with CreativeWorkSeries is on
     published materials (written e.g. books and periodicals, or media such as TV, radio and games). Specific
     subtypes are available for describing [[TVSeries]], [[RadioSeries]], [[MovieSeries]], [[BookSeries]],
     [[Periodical]] and [[VideoGameSeries]]. In each case, the [[hasPart]] / [[isPartOf]] properties can be
     used to relate the CreativeWorkSeries to its parts. The general CreativeWorkSeries type serves largely
     just to organize these more specific and practical subtypes. It is common for properties applicable to an
     item from the series to be usefully applied to the containing group. Schema.org attempts to anticipate some
     of these cases, but publishers should be free to apply properties of the series parts to the series as a whole
     wherever they seem appropriate.

    See: https://schema.org/CreativeWorkSeries
    Model depth: 3
    """

    type_: str = Field(default="CreativeWorkSeries", alias="@type", const=True)
    issn: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The International Standard Serial Number (ISSN) that identifies this serial publication. You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L) for, this serial publication.",
    )
    endDate: Optional[
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
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    startDate: Optional[
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
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Date import Date
