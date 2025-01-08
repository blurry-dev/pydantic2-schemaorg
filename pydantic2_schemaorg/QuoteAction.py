from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.TradeAction import TradeAction


class QuoteAction(TradeAction):
    """An agent quotes/estimates/appraises an object/product/service with a price at a location/store.

    See: https://schema.org/QuoteAction
    Model depth: 4
    """

    type_: str = Field(default="QuoteAction", alias="@type", const=True)
