from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AdultOrientedEnumeration import AdultOrientedEnumeration


class ViolenceConsideration(AdultOrientedEnumeration):
    """Item shows or promotes violence.

    See: https://schema.org/ViolenceConsideration
    Model depth: 5
    """

    type_: str = Field(default="ViolenceConsideration", alias="@type", const=True)
