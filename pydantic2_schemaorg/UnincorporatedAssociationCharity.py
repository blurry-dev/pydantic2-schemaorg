from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.UKNonprofitType import UKNonprofitType


class UnincorporatedAssociationCharity(UKNonprofitType):
    """UnincorporatedAssociationCharity: Non-profit type referring to a charitable company that is not incorporated
     (UK).

    See: https://schema.org/UnincorporatedAssociationCharity
    Model depth: 6
    """

    type_: str = Field(
        default="UnincorporatedAssociationCharity", alias="@type", const=True
    )
