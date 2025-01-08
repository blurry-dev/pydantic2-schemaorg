from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class Property(Intangible):
    """A property, used to indicate attributes and relationships of some Thing; equivalent to rdf:Property.

    See: https://schema.org/Property
    Model depth: 3
    """

    type_: str = Field(default="Property", alias="@type", const=True)
    inverseOf: Optional[Union[List[Union["Property", str]], "Property", str]] = Field(
        default=None,
        description="Relates a property to a property that is its inverse. Inverse properties relate the same pairs of items to each other, but in reversed direction. For example, the 'alumni' and 'alumniOf' properties are inverseOf each other. Some properties don't have explicit inverses; in these situations RDFa and JSON-LD syntax for reverse properties can be used.",
    )
    rangeIncludes: Optional[Union[List[Union["Class", str]], "Class", str]] = Field(
        default=None,
        description="Relates a property to a class that constitutes (one of) the expected type(s) for values of the property.",
    )
    supersededBy: Optional[
        Union[
            List[Union["Class", "Enumeration", "Property", str]],
            "Class",
            "Enumeration",
            "Property",
            str,
        ]
    ] = Field(
        default=None,
        description="Relates a term (i.e. a property, class or enumeration) to one that supersedes it.",
    )
    domainIncludes: Optional[Union[List[Union["Class", str]], "Class", str]] = Field(
        default=None,
        description="Relates a property to a class that is (one of) the type(s) the property is expected to be used on.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Class import Class
    from pydantic2_schemaorg.Enumeration import Enumeration
