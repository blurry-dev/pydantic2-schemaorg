from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic.v1 import AnyUrl
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Thing import Thing


class Taxon(Thing):
    """A set of organisms asserted to represent a natural cohesive biological unit.

    See: https://schema.org/Taxon
    Model depth: 2
    """

    type_: str = Field(default="Taxon", alias="@type", const=True)
    taxonRank: Optional[
        Union[
            List[Union[AnyUrl, "URL", str, "Text", "PropertyValue"]],
            AnyUrl,
            "URL",
            str,
            "Text",
            "PropertyValue",
        ]
    ] = Field(
        default=None,
        description="The taxonomic rank of this taxon given preferably as a URI from a controlled vocabulary – typically the ranks from TDWG TaxonRank ontology or equivalent Wikidata URIs.",
    )
    hasDefinedTerm: Optional[
        Union[List[Union["DefinedTerm", str]], "DefinedTerm", str]
    ] = Field(
        default=None,
        description="A Defined Term contained in this term set.",
    )
    parentTaxon: Optional[
        Union[
            List[Union[AnyUrl, "URL", str, "Text", "Taxon"]],
            AnyUrl,
            "URL",
            str,
            "Text",
            "Taxon",
        ]
    ] = Field(
        default=None,
        description="Closest parent taxon of the taxon in question.",
    )
    childTaxon: Optional[
        Union[
            List[Union[AnyUrl, "URL", str, "Text", "Taxon"]],
            AnyUrl,
            "URL",
            str,
            "Text",
            "Taxon",
        ]
    ] = Field(
        default=None,
        description="Closest child taxa of the taxon in question.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.PropertyValue import PropertyValue
    from pydantic2_schemaorg.DefinedTerm import DefinedTerm
