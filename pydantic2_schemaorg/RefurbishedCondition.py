from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.OfferItemCondition import OfferItemCondition


class RefurbishedCondition(OfferItemCondition):
    """Indicates that the item is refurbished.

    See: https://schema.org/RefurbishedCondition
    Model depth: 5
    """

    type_: str = Field(default="RefurbishedCondition", alias="@type", const=True)
