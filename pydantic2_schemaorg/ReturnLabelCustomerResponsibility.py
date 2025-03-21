from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ReturnLabelSourceEnumeration import (
    ReturnLabelSourceEnumeration,
)


class ReturnLabelCustomerResponsibility(ReturnLabelSourceEnumeration):
    """Indicated that creating a return label is the responsibility of the customer.

    See: https://schema.org/ReturnLabelCustomerResponsibility
    Model depth: 5
    """

    type_: str = Field(
        default="ReturnLabelCustomerResponsibility", alias="@type", const=True
    )
