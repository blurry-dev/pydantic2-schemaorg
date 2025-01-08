from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class ServiceChannel(Intangible):
    """A means for accessing a service, e.g. a government office location, web site, or phone number.

    See: https://schema.org/ServiceChannel
    Model depth: 3
    """

    type_: str = Field(default="ServiceChannel", alias="@type", const=True)
    availableLanguage: Optional[
        Union[List[Union[str, "Text", "Language"]], str, "Text", "Language"]
    ] = Field(
        default=None,
        description="A language someone may use with or at the item, service or place. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[inLanguage]].",
    )
    serviceLocation: Optional[Union[List[Union["Place", str]], "Place", str]] = Field(
        default=None,
        description="The location (e.g. civic structure, local business, etc.) where a person can go to access the service.",
    )
    serviceUrl: Optional[Union[List[Union[AnyUrl, "URL", str]], AnyUrl, "URL", str]] = (
        Field(
            default=None,
            description="The website to access the service.",
        )
    )
    serviceSmsNumber: Optional[
        Union[List[Union["ContactPoint", str]], "ContactPoint", str]
    ] = Field(
        default=None,
        description="The number to access the service by text message.",
    )
    servicePostalAddress: Optional[
        Union[List[Union["PostalAddress", str]], "PostalAddress", str]
    ] = Field(
        default=None,
        description="The address for accessing the service by mail.",
    )
    providesService: Optional[Union[List[Union["Service", str]], "Service", str]] = (
        Field(
            default=None,
            description="The service provided by this channel.",
        )
    )
    processingTime: Optional[Union[List[Union["Duration", str]], "Duration", str]] = (
        Field(
            default=None,
            description="Estimated processing time for the service using this channel.",
        )
    )
    servicePhone: Optional[
        Union[List[Union["ContactPoint", str]], "ContactPoint", str]
    ] = Field(
        default=None,
        description="The phone number to use to access the service.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Language import Language
    from pydantic2_schemaorg.Place import Place
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.ContactPoint import ContactPoint
    from pydantic2_schemaorg.PostalAddress import PostalAddress
    from pydantic2_schemaorg.Service import Service
    from pydantic2_schemaorg.Duration import Duration
