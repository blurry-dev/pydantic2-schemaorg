from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AdultOrientedEnumeration import AdultOrientedEnumeration


class WeaponConsideration(AdultOrientedEnumeration):
    """The item is intended to induce bodily harm, for example guns, mace, combat knives, brass knuckles, nail or
     other bombs, and spears.

    See: https://schema.org/WeaponConsideration
    Model depth: 5
    """

    type_: str = Field(default="WeaponConsideration", alias="@type", const=True)
