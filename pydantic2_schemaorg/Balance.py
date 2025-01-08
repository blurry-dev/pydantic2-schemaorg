from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory


class Balance(PhysicalActivityCategory):
    """Physical activity that is engaged to help maintain posture and balance.

    See: https://schema.org/Balance
    Model depth: 5
    """

    type_: str = Field(default="Balance", alias="@type", const=True)
