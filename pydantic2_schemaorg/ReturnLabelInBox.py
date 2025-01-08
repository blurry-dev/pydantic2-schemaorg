from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ReturnLabelSourceEnumeration import (
    ReturnLabelSourceEnumeration,
)


class ReturnLabelInBox(ReturnLabelSourceEnumeration):
    """Specifies that a return label will be provided by the seller in the shipping box.

    See: https://schema.org/ReturnLabelInBox
    Model depth: 5
    """

    type_: str = Field(default="ReturnLabelInBox", alias="@type", const=True)
