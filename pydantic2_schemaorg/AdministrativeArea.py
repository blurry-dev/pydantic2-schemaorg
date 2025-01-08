from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Place import Place


class AdministrativeArea(Place):
    """A geographical region, typically under the jurisdiction of a particular government.

    See: https://schema.org/AdministrativeArea
    Model depth: 3
    """

    type_: str = Field(default="AdministrativeArea", alias="@type", const=True)
