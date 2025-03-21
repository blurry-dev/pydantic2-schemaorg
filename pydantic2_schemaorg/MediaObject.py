from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import date, datetime, time
from typing import List, Optional, Union
from pydantic.v1 import AnyUrl, StrictBool


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class MediaObject(CreativeWork):
    """A media object, such as an image, video, audio, or text object embedded in a web page or a downloadable dataset
     i.e. DataDownload. Note that a creative work may have many media objects associated with it on the same web
     page. For example, a page about a single song (MusicRecording) may have a music video (VideoObject), and a
     high and low bandwidth audio stream (2 AudioObject's).

    See: https://schema.org/MediaObject
    Model depth: 3
    """

    type_: str = Field(default="MediaObject", alias="@type", const=True)
    uploadDate: Optional[
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
        description="Date (including time if available) when this media object was uploaded to this site.",
    )
    encodingFormat: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description="Media type typically expressed using a MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml) and [MDN reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)), e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc. In cases where a [[CreativeWork]] has several media type representations, [[encoding]] can be used to indicate each [[MediaObject]] alongside particular [[encodingFormat]] information. Unregistered or niche encoding and file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry.",
    )
    duration: Optional[Union[List[Union["Duration", str]], "Duration", str]] = Field(
        default=None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    associatedArticle: Optional[
        Union[List[Union["NewsArticle", str]], "NewsArticle", str]
    ] = Field(
        default=None,
        description="A NewsArticle associated with the Media Object.",
    )
    productionCompany: Optional[
        Union[List[Union["Organization", str]], "Organization", str]
    ] = Field(
        default=None,
        description="The production company or studio responsible for the item, e.g. series, video game, episode etc.",
    )
    interpretedAsClaim: Optional[Union[List[Union["Claim", str]], "Claim", str]] = (
        Field(
            default=None,
            description="Used to indicate a specific claim contained, implied, translated or refined from the content of a [[MediaObject]] or other [[CreativeWork]]. The interpreting party can be indicated using [[claimInterpreter]].",
        )
    )
    contentUrl: Optional[Union[List[Union[AnyUrl, "URL", str]], AnyUrl, "URL", str]] = (
        Field(
            default=None,
            description="Actual bytes of the media object, for example the image file or video file.",
        )
    )
    contentSize: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="File size in (mega/kilo)bytes.",
    )
    playerType: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Player type required&#x2014;for example, Flash or Silverlight.",
    )
    startTime: Optional[
        Union[
            List[Union[datetime, "DateTime", time, "Time", str]],
            datetime,
            "DateTime",
            time,
            "Time",
            str,
        ]
    ] = Field(
        default=None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. E.g. John wrote a book from *January* to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file. Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.",
    )
    endTime: Optional[
        Union[
            List[Union[datetime, "DateTime", time, "Time", str]],
            datetime,
            "DateTime",
            time,
            "Time",
            str,
        ]
    ] = Field(
        default=None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. E.g. John wrote a book from January to *December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file. Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.",
    )
    width: Optional[
        Union[
            List[Union["Distance", "QuantitativeValue", str]],
            "Distance",
            "QuantitativeValue",
            str,
        ]
    ] = Field(
        default=None,
        description="The width of the item.",
    )
    sha256: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The [SHA-2](https://en.wikipedia.org/wiki/SHA-2) SHA256 hash of the content of the item. For example, a zero-length input has value 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'.",
    )
    bitrate: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The bitrate of the media object.",
    )
    embedUrl: Optional[Union[List[Union[AnyUrl, "URL", str]], AnyUrl, "URL", str]] = (
        Field(
            default=None,
            description="A URL pointing to a player for a specific video. In general, this is the information in the ```src``` element of an ```embed``` tag and should not be the same as the content of the ```loc``` tag.",
        )
    )
    requiresSubscription: Optional[
        Union[
            List[Union[StrictBool, "Boolean", "MediaSubscription", str]],
            StrictBool,
            "Boolean",
            "MediaSubscription",
            str,
        ]
    ] = Field(
        default=None,
        description="Indicates if use of the media require a subscription (either paid or free). Allowed values are ```true``` or ```false``` (note that an earlier version had 'yes', 'no').",
    )
    height: Optional[
        Union[
            List[Union["Distance", "QuantitativeValue", str]],
            "Distance",
            "QuantitativeValue",
            str,
        ]
    ] = Field(
        default=None,
        description="The height of the item.",
    )
    encodesCreativeWork: Optional[
        Union[List[Union["CreativeWork", str]], "CreativeWork", str]
    ] = Field(
        default=None,
        description="The CreativeWork encoded by this media object.",
    )
    regionsAllowed: Optional[Union[List[Union["Place", str]], "Place", str]] = Field(
        default=None,
        description="The regions where the media is allowed. If not specified, then it's assumed to be allowed everywhere. Specify the countries in [ISO 3166 format](http://en.wikipedia.org/wiki/ISO_3166).",
    )
    ineligibleRegion: Optional[
        Union[
            List[Union[str, "Text", "Place", "GeoShape"]],
            str,
            "Text",
            "Place",
            "GeoShape",
        ]
    ] = Field(
        default=None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed. See also [[eligibleRegion]].",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Date import Date
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Duration import Duration
    from pydantic2_schemaorg.NewsArticle import NewsArticle
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.Claim import Claim
    from pydantic2_schemaorg.Time import Time
    from pydantic2_schemaorg.Distance import Distance
    from pydantic2_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic2_schemaorg.Boolean import Boolean
    from pydantic2_schemaorg.MediaSubscription import MediaSubscription
    from pydantic2_schemaorg.CreativeWork import CreativeWork
    from pydantic2_schemaorg.Place import Place
    from pydantic2_schemaorg.GeoShape import GeoShape
