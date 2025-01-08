from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration


class ReturnFeesCustomerResponsibility(ReturnFeesEnumeration):
    """Specifies that product returns must be paid for, and are the responsibility of, the customer.

    See: https://schema.org/ReturnFeesCustomerResponsibility
    Model depth: 5
    """

    type_: str = Field(
        default="ReturnFeesCustomerResponsibility", alias="@type", const=True
    )
