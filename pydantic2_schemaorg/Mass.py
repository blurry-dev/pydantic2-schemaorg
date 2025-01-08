from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Quantity import Quantity


class Mass(Quantity):
    """Properties that take Mass as values are of the form '&lt;Number&gt; &lt;Mass unit of measure&gt;'. E.g.,
     '7 kg'.

    See: https://schema.org/Mass
    Model depth: 4
    """

    type_: str = Field(default="Mass", alias="@type", const=True)
