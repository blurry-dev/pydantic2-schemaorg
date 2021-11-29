from pydantic import AnyUrl, Field
from typing import List, Optional, Union, Any
from pydantic_schemaorg.Organization import Organization


class SportsOrganization(Organization):
    """Represents the collection of all sports organizations, including sports teams, governing"
     "bodies, and sports associations.

    See https://schema.org/SportsOrganization.

    """

    sport: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="A type of sport (e.g. Baseball).",
    )
    locals().update({"@type": Field("SportsOrganization", const=True)})


SportsOrganization.update_forward_refs()