from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic.v1 import AnyUrl
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class ConstraintNode(Intangible):
    """The ConstraintNode type is provided to support usecases in which a node in a structured data graph is described
     with properties which appear to describe a single entity, but are being used in a situation where they serve
     a more abstract purpose. A [[ConstraintNode]] can be described using [[constraintProperty]] and [[numConstraints]].
     These constraint properties can serve a variety of purposes, and their values may sometimes be understood
     to indicate sets of possible values rather than single, exact and specific values.

    See: https://schema.org/ConstraintNode
    Model depth: 3
    """

    type_: str = Field(default="ConstraintNode", alias="@type", const=True)
    constraintProperty: Optional[
        Union[
            List[Union[AnyUrl, "URL", "Property", str]], AnyUrl, "URL", "Property", str
        ]
    ] = Field(
        default=None,
        description="Indicates a property used as a constraint. For example, in the definition of a [[StatisticalVariable]]. The value is a property, either from within Schema.org or from other compatible (e.g. RDF) systems such as DataCommons.org or Wikidata.org.",
    )
    numConstraints: Optional[
        Union[List[Union[int, "Integer", str]], int, "Integer", str]
    ] = Field(
        default=None,
        description="Indicates the number of constraints property values defined for a particular [[ConstraintNode]] such as [[StatisticalVariable]]. This helps applications understand if they have access to a sufficiently complete description of a [[StatisticalVariable]] or other construct that is defined using properties on template-style nodes.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.Property import Property
    from pydantic2_schemaorg.Integer import Integer
