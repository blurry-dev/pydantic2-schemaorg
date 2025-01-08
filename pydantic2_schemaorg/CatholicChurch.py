from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Church import Church


class CatholicChurch(Church):
    """A Catholic church.

    See: https://schema.org/CatholicChurch
    Model depth: 6
    """

    type_: str = Field(default="CatholicChurch", alias="@type", const=True)
