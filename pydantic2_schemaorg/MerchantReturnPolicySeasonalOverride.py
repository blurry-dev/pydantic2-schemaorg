from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import date, datetime
from typing import List, Optional, Union
from pydantic.v1 import StrictInt, StrictFloat


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class MerchantReturnPolicySeasonalOverride(Intangible):
    """A seasonal override of a return policy, for example used for holidays.

    See: https://schema.org/MerchantReturnPolicySeasonalOverride
    Model depth: 3
    """

    type_: str = Field(
        default="MerchantReturnPolicySeasonalOverride", alias="@type", const=True
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
    refundType: Optional[
        Union[List[Union["RefundTypeEnumeration", str]], "RefundTypeEnumeration", str]
    ] = Field(
        default=None,
        description="A refund type, from an enumerated list.",
    )
    restockingFee: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", "MonetaryAmount", str]],
            StrictInt,
            StrictFloat,
            "Number",
            "MonetaryAmount",
            str,
        ]
    ] = Field(
        default=None,
        description="Use [[MonetaryAmount]] to specify a fixed restocking fee for product returns, or use [[Number]] to specify a percentage of the product price paid by the customer.",
    )
    merchantReturnDays: Optional[
        Union[
            List[Union[datetime, "DateTime", int, "Integer", date, "Date", str]],
            datetime,
            "DateTime",
            int,
            "Integer",
            date,
            "Date",
            str,
        ]
    ] = Field(
        default=None,
        description="Specifies either a fixed return date or the number of days (from the delivery date) that a product can be returned. Used when the [[returnPolicyCategory]] property is specified as [[MerchantReturnFiniteReturnWindow]].",
    )
    returnFees: Optional[
        Union[List[Union["ReturnFeesEnumeration", str]], "ReturnFeesEnumeration", str]
    ] = Field(
        default=None,
        description="The type of return fees for purchased products (for any return reason).",
    )
    returnShippingFeesAmount: Optional[
        Union[List[Union["MonetaryAmount", str]], "MonetaryAmount", str]
    ] = Field(
        default=None,
        description="Amount of shipping costs for product returns (for any reason). Applicable when property [[returnFees]] equals [[ReturnShippingFees]].",
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
    returnMethod: Optional[
        Union[
            List[Union["ReturnMethodEnumeration", str]], "ReturnMethodEnumeration", str
        ]
    ] = Field(
        default=None,
        description="The type of return method offered, specified from an enumeration.",
    )
    returnPolicyCategory: Optional[
        Union[
            List[Union["MerchantReturnEnumeration", str]],
            "MerchantReturnEnumeration",
            str,
        ]
    ] = Field(
        default=None,
        description="Specifies an applicable return policy (from an enumeration).",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Date import Date
    from pydantic2_schemaorg.RefundTypeEnumeration import RefundTypeEnumeration
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic2_schemaorg.Integer import Integer
    from pydantic2_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration
    from pydantic2_schemaorg.ReturnMethodEnumeration import ReturnMethodEnumeration
    from pydantic2_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration
