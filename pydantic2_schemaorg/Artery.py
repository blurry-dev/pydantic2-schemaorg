from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Vessel import Vessel


class Artery(Vessel):
    """A type of blood vessel that specifically carries blood away from the heart.

    See: https://schema.org/Artery
    Model depth: 5
    """

    type_: str = Field(default="Artery", alias="@type", const=True)
    arterialBranch: Optional[
        Union[List[Union["AnatomicalStructure", str]], "AnatomicalStructure", str]
    ] = Field(
        default=None,
        description="The branches that comprise the arterial structure.",
    )
    supplyTo: Optional[
        Union[List[Union["AnatomicalStructure", str]], "AnatomicalStructure", str]
    ] = Field(
        default=None,
        description="The area to which the artery supplies blood.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.AnatomicalStructure import AnatomicalStructure
