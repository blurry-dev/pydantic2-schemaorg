from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Collection import Collection
from pydantic2_schemaorg.Product import Product


class ProductCollection(Collection, Product):
    """A set of products (either [[ProductGroup]]s or specific variants) that are listed together e.g. in an [[Offer]].

    See: https://schema.org/ProductCollection
    Model depth: 3
    """

    type_: str = Field(default="ProductCollection", alias="@type", const=True)
    includesObject: Optional[
        Union[List[Union["TypeAndQuantityNode", str]], "TypeAndQuantityNode", str]
    ] = Field(
        default=None,
        description="This links to a node or nodes indicating the exact quantity of the products included in an [[Offer]] or [[ProductCollection]].",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.TypeAndQuantityNode import TypeAndQuantityNode
