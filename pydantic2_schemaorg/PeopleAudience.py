from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import StrictInt, StrictFloat


from pydantic.v1 import Field
from pydantic2_schemaorg.Audience import Audience


class PeopleAudience(Audience):
    """A set of characteristics belonging to people, e.g. who compose an item's target audience.

    See: https://schema.org/PeopleAudience
    Model depth: 4
    """

    type_: str = Field(default="PeopleAudience", alias="@type", const=True)
    healthCondition: Optional[
        Union[List[Union["MedicalCondition", str]], "MedicalCondition", str]
    ] = Field(
        default=None,
        description="Specifying the health condition(s) of a patient, medical study, or other target audience.",
    )
    requiredGender: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Audiences defined by a person's gender.",
    )
    suggestedGender: Optional[
        Union[List[Union[str, "Text", "GenderType"]], str, "Text", "GenderType"]
    ] = Field(
        default=None,
        description='The suggested gender of the intended person or audience, for example "male", "female", or "unisex".',
    )
    suggestedMaxAge: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", str]],
            StrictInt,
            StrictFloat,
            "Number",
            str,
        ]
    ] = Field(
        default=None,
        description="Maximum recommended age in years for the audience or user.",
    )
    requiredMinAge: Optional[
        Union[List[Union[int, "Integer", str]], int, "Integer", str]
    ] = Field(
        default=None,
        description="Audiences defined by a person's minimum age.",
    )
    suggestedAge: Optional[
        Union[List[Union["QuantitativeValue", str]], "QuantitativeValue", str]
    ] = Field(
        default=None,
        description="The age or age range for the intended audience or person, for example 3-12 months for infants, 1-5 years for toddlers.",
    )
    suggestedMeasurement: Optional[
        Union[List[Union["QuantitativeValue", str]], "QuantitativeValue", str]
    ] = Field(
        default=None,
        description="A suggested range of body measurements for the intended audience or person, for example inseam between 32 and 34 inches or height between 170 and 190 cm. Typically found on a size chart for wearable products.",
    )
    requiredMaxAge: Optional[
        Union[List[Union[int, "Integer", str]], int, "Integer", str]
    ] = Field(
        default=None,
        description="Audiences defined by a person's maximum age.",
    )
    suggestedMinAge: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", str]],
            StrictInt,
            StrictFloat,
            "Number",
            str,
        ]
    ] = Field(
        default=None,
        description="Minimum recommended age in years for the audience or user.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.MedicalCondition import MedicalCondition
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.GenderType import GenderType
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.Integer import Integer
    from pydantic2_schemaorg.QuantitativeValue import QuantitativeValue
