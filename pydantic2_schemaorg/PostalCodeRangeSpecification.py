from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.StructuredValue import StructuredValue


class PostalCodeRangeSpecification(StructuredValue):
    """Indicates a range of postal codes, usually defined as the set of valid codes between [[postalCodeBegin]]
     and [[postalCodeEnd]], inclusively.

    See: https://schema.org/PostalCodeRangeSpecification
    Model depth: 4
    """

    type_: str = Field(
        default="PostalCodeRangeSpecification", alias="@type", const=True
    )
    postalCodeBegin: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="First postal code in a range (included).",
    )
    postalCodeEnd: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Last postal code in the range (included). Needs to be after [[postalCodeBegin]].",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
