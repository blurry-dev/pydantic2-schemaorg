from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AdultOrientedEnumeration import AdultOrientedEnumeration


class SexualContentConsideration(AdultOrientedEnumeration):
    """The item contains sexually oriented content such as nudity, suggestive or explicit material, or related
     online services, or is intended to enhance sexual activity. Examples: Erotic videos or magazine, sexual
     enhancement devices, sex toys.

    See: https://schema.org/SexualContentConsideration
    Model depth: 5
    """

    type_: str = Field(default="SexualContentConsideration", alias="@type", const=True)
