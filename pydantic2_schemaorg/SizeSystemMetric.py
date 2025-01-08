from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.SizeSystemEnumeration import SizeSystemEnumeration


class SizeSystemMetric(SizeSystemEnumeration):
    """Metric size system.

    See: https://schema.org/SizeSystemMetric
    Model depth: 5
    """

    type_: str = Field(default="SizeSystemMetric", alias="@type", const=True)
