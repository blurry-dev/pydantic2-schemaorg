from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.StructuredValue import StructuredValue


class ContactPoint(StructuredValue):
    """A contact point&#x2014;for example, a Customer Complaints department.

    See: https://schema.org/ContactPoint
    Model depth: 4
    """

    type_: str = Field(default="ContactPoint", alias="@type", const=True)
    faxNumber: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The fax number.",
    )
    availableLanguage: Optional[
        Union[List[Union[str, "Text", "Language"]], str, "Text", "Language"]
    ] = Field(
        default=None,
        description="A language someone may use with or at the item, service or place. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[inLanguage]].",
    )
    contactOption: Optional[
        Union[List[Union["ContactPointOption", str]], "ContactPointOption", str]
    ] = Field(
        default=None,
        description="An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers).",
    )
    contactType: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="A person or organization can have different contact points, for different purposes. For example, a sales contact point, a PR contact point and so on. This property is used to specify the kind of contact point.",
    )
    productSupported: Optional[
        Union[List[Union[str, "Text", "Product"]], str, "Text", "Product"]
    ] = Field(
        default=None,
        description='The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. "iPhone") or a general category of products or services (e.g. "smartphones").',
    )
    serviceArea: Optional[
        Union[
            List[Union["Place", "GeoShape", "AdministrativeArea", str]],
            "Place",
            "GeoShape",
            "AdministrativeArea",
            str,
        ]
    ] = Field(
        default=None,
        description="The geographic area where the service is provided.",
    )
    hoursAvailable: Optional[
        Union[
            List[Union["OpeningHoursSpecification", str]],
            "OpeningHoursSpecification",
            str,
        ]
    ] = Field(
        default=None,
        description="The hours during which this service or contact is available.",
    )
    email: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Email address.",
    )
    areaServed: Optional[
        Union[
            List[Union[str, "Text", "Place", "GeoShape", "AdministrativeArea"]],
            str,
            "Text",
            "Place",
            "GeoShape",
            "AdministrativeArea",
        ]
    ] = Field(
        default=None,
        description="The geographic area where a service or offered item is provided.",
    )
    telephone: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The telephone number.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Language import Language
    from pydantic2_schemaorg.ContactPointOption import ContactPointOption
    from pydantic2_schemaorg.Product import Product
    from pydantic2_schemaorg.Place import Place
    from pydantic2_schemaorg.GeoShape import GeoShape
    from pydantic2_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic2_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification
