from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import datetime


from pydantic.v1 import Field
from pydantic2_schemaorg.StructuredValue import StructuredValue


class OwnershipInfo(StructuredValue):
    """A structured value providing information about when a certain organization or person owned a certain product.

    See: https://schema.org/OwnershipInfo
    Model depth: 4
    """

    type_: str = Field(default="OwnershipInfo", alias="@type", const=True)
    acquiredFrom: Optional[
        Union[List[Union["Person", "Organization", str]], "Person", "Organization", str]
    ] = Field(
        default=None,
        description="The organization or person from which the product was acquired.",
    )
    ownedThrough: Optional[
        Union[List[Union[datetime, "DateTime", str]], datetime, "DateTime", str]
    ] = Field(
        default=None,
        description="The date and time of giving up ownership on the product.",
    )
    ownedFrom: Optional[
        Union[List[Union[datetime, "DateTime", str]], datetime, "DateTime", str]
    ] = Field(
        default=None,
        description="The date and time of obtaining the product.",
    )
    typeOfGood: Optional[
        Union[List[Union["Service", "Product", str]], "Service", "Product", str]
    ] = Field(
        default=None,
        description="The product that this structured value is referring to.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Service import Service
    from pydantic2_schemaorg.Product import Product
