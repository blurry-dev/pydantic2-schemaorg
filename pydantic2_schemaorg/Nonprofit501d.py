from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501d(USNonprofitType):
    """Nonprofit501d: Non-profit type referring to Religious and Apostolic Associations.

    See: https://schema.org/Nonprofit501d
    Model depth: 6
    """

    type_: str = Field(default="Nonprofit501d", alias="@type", const=True)
