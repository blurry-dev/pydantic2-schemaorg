from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.TradeAction import TradeAction


class BuyAction(TradeAction):
    """The act of giving money to a seller in exchange for goods or services rendered. An agent buys an object, product,
     or service from a seller for a price. Reciprocal of SellAction.

    See: https://schema.org/BuyAction
    Model depth: 4
    """

    type_: str = Field(default="BuyAction", alias="@type", const=True)
    seller: Optional[
        Union[List[Union["Person", "Organization", str]], "Person", "Organization", str]
    ] = Field(
        default=None,
        description="An entity which offers (sells / leases / lends / loans) the services / goods. A seller may also be a provider.",
    )
    vendor: Optional[
        Union[List[Union["Person", "Organization", str]], "Person", "Organization", str]
    ] = Field(
        default=None,
        description="'vendor' is an earlier term for 'seller'.",
    )
    warrantyPromise: Optional[
        Union[List[Union["WarrantyPromise", str]], "WarrantyPromise", str]
    ] = Field(
        default=None,
        description="The warranty promise(s) included in the offer.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.WarrantyPromise import WarrantyPromise
