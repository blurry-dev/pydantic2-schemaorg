from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.StructuredValue import StructuredValue


class NutritionInformation(StructuredValue):
    """Nutritional information about the recipe.

    See: https://schema.org/NutritionInformation
    Model depth: 4
    """

    type_: str = Field(default="NutritionInformation", alias="@type", const=True)
    transFatContent: Optional[Union[List[Union["Mass", str]], "Mass", str]] = Field(
        default=None,
        description="The number of grams of trans fat.",
    )
    sugarContent: Optional[Union[List[Union["Mass", str]], "Mass", str]] = Field(
        default=None,
        description="The number of grams of sugar.",
    )
    unsaturatedFatContent: Optional[Union[List[Union["Mass", str]], "Mass", str]] = (
        Field(
            default=None,
            description="The number of grams of unsaturated fat.",
        )
    )
    fatContent: Optional[Union[List[Union["Mass", str]], "Mass", str]] = Field(
        default=None,
        description="The number of grams of fat.",
    )
    fiberContent: Optional[Union[List[Union["Mass", str]], "Mass", str]] = Field(
        default=None,
        description="The number of grams of fiber.",
    )
    sodiumContent: Optional[Union[List[Union["Mass", str]], "Mass", str]] = Field(
        default=None,
        description="The number of milligrams of sodium.",
    )
    cholesterolContent: Optional[Union[List[Union["Mass", str]], "Mass", str]] = Field(
        default=None,
        description="The number of milligrams of cholesterol.",
    )
    carbohydrateContent: Optional[Union[List[Union["Mass", str]], "Mass", str]] = Field(
        default=None,
        description="The number of grams of carbohydrates.",
    )
    servingSize: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The serving size, in terms of the number of volume or mass.",
    )
    calories: Optional[Union[List[Union["Energy", str]], "Energy", str]] = Field(
        default=None,
        description="The number of calories.",
    )
    saturatedFatContent: Optional[Union[List[Union["Mass", str]], "Mass", str]] = Field(
        default=None,
        description="The number of grams of saturated fat.",
    )
    proteinContent: Optional[Union[List[Union["Mass", str]], "Mass", str]] = Field(
        default=None,
        description="The number of grams of protein.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Mass import Mass
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Energy import Energy
