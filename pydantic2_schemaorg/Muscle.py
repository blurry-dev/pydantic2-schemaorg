from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.AnatomicalStructure import AnatomicalStructure


class Muscle(AnatomicalStructure):
    """A muscle is an anatomical structure consisting of a contractile form of tissue that animals use to effect movement.

    See: https://schema.org/Muscle
    Model depth: 4
    """

    type_: str = Field(default="Muscle", alias="@type", const=True)
    muscleAction: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The movement the muscle generates.",
    )
    insertion: Optional[
        Union[List[Union["AnatomicalStructure", str]], "AnatomicalStructure", str]
    ] = Field(
        default=None,
        description="The place of attachment of a muscle, or what the muscle moves.",
    )
    nerve: Optional[Union[List[Union["Nerve", str]], "Nerve", str]] = Field(
        default=None,
        description="The underlying innervation associated with the muscle.",
    )
    bloodSupply: Optional[Union[List[Union["Vessel", str]], "Vessel", str]] = Field(
        default=None,
        description="The blood vessel that carries blood from the heart to the muscle.",
    )
    antagonist: Optional[Union[List[Union["Muscle", str]], "Muscle", str]] = Field(
        default=None,
        description="The muscle whose action counteracts the specified muscle.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.AnatomicalStructure import AnatomicalStructure
    from pydantic2_schemaorg.Nerve import Nerve
    from pydantic2_schemaorg.Vessel import Vessel
