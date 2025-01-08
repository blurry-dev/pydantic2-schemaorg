from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Organization import Organization


class OnlineBusiness(Organization):
    """A particular online business, either standalone or the online part of a broader organization. Examples include
     an eCommerce site, an online travel booking site, an online learning site, an online logistics and shipping
     provider, an online (virtual) doctor, etc.

    See: https://schema.org/OnlineBusiness
    Model depth: 3
    """

    type_: str = Field(default="OnlineBusiness", alias="@type", const=True)
