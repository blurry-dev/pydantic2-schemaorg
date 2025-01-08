from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class RestrictedDiet(Enumeration):
    """A diet restricted to certain foods or preparations for cultural, religious, health or lifestyle reasons.

    See: https://schema.org/RestrictedDiet
    Model depth: 4
    """

    type_: str = Field(default="RestrictedDiet", alias="@type", const=True)
