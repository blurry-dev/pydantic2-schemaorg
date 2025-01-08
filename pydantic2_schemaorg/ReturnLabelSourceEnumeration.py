from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class ReturnLabelSourceEnumeration(Enumeration):
    """Enumerates several types of return labels for product returns.

    See: https://schema.org/ReturnLabelSourceEnumeration
    Model depth: 4
    """

    type_: str = Field(
        default="ReturnLabelSourceEnumeration", alias="@type", const=True
    )
