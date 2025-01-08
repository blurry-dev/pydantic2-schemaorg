from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AdultOrientedEnumeration import AdultOrientedEnumeration


class UnclassifiedAdultConsideration(AdultOrientedEnumeration):
    """The item is suitable only for adults, without indicating why. Due to widespread use of \"adult\" as a euphemism
     for \"sexual\", many such items are likely suited also for the SexualContentConsideration code.

    See: https://schema.org/UnclassifiedAdultConsideration
    Model depth: 5
    """

    type_: str = Field(
        default="UnclassifiedAdultConsideration", alias="@type", const=True
    )
