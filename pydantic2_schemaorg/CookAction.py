from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.CreateAction import CreateAction


class CookAction(CreateAction):
    """The act of producing/preparing food.

    See: https://schema.org/CookAction
    Model depth: 4
    """

    type_: str = Field(default="CookAction", alias="@type", const=True)
    foodEstablishment: Optional[
        Union[
            List[Union["Place", "FoodEstablishment", str]],
            "Place",
            "FoodEstablishment",
            str,
        ]
    ] = Field(
        default=None,
        description="A sub property of location. The specific food establishment where the action occurred.",
    )
    foodEvent: Optional[Union[List[Union["FoodEvent", str]], "FoodEvent", str]] = Field(
        default=None,
        description="A sub property of location. The specific food event where the action occurred.",
    )
    recipe: Optional[Union[List[Union["Recipe", str]], "Recipe", str]] = Field(
        default=None,
        description="A sub property of instrument. The recipe/instructions used to perform the action.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Place import Place
    from pydantic2_schemaorg.FoodEstablishment import FoodEstablishment
    from pydantic2_schemaorg.FoodEvent import FoodEvent
    from pydantic2_schemaorg.Recipe import Recipe
