from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.PlayAction import PlayAction


class ExerciseAction(PlayAction):
    """The act of participating in exertive activity for the purposes of improving health and fitness.

    See: https://schema.org/ExerciseAction
    Model depth: 4
    """

    type_: str = Field(default="ExerciseAction", alias="@type", const=True)
    exercisePlan: Optional[
        Union[List[Union["ExercisePlan", str]], "ExercisePlan", str]
    ] = Field(
        default=None,
        description="A sub property of instrument. The exercise plan used on this action.",
    )
    exerciseCourse: Optional[Union[List[Union["Place", str]], "Place", str]] = Field(
        default=None,
        description="A sub property of location. The course where this action was taken.",
    )
    sportsActivityLocation: Optional[
        Union[List[Union["SportsActivityLocation", str]], "SportsActivityLocation", str]
    ] = Field(
        default=None,
        description="A sub property of location. The sports activity location where this action occurred.",
    )
    exerciseType: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Type(s) of exercise or activity, such as strength training, flexibility training, aerobics, cardiac rehabilitation, etc.",
    )
    opponent: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="A sub property of participant. The opponent on this action.",
    )
    exerciseRelatedDiet: Optional[Union[List[Union["Diet", str]], "Diet", str]] = Field(
        default=None,
        description="A sub property of instrument. The diet used in this action.",
    )
    diet: Optional[Union[List[Union["Diet", str]], "Diet", str]] = Field(
        default=None,
        description="A sub property of instrument. The diet used in this action.",
    )
    course: Optional[Union[List[Union["Place", str]], "Place", str]] = Field(
        default=None,
        description="A sub property of location. The course where this action was taken.",
    )
    toLocation: Optional[Union[List[Union["Place", str]], "Place", str]] = Field(
        default=None,
        description="A sub property of location. The final location of the object or the agent after the action.",
    )
    sportsTeam: Optional[Union[List[Union["SportsTeam", str]], "SportsTeam", str]] = (
        Field(
            default=None,
            description="A sub property of participant. The sports team that participated on this action.",
        )
    )
    fromLocation: Optional[Union[List[Union["Place", str]], "Place", str]] = Field(
        default=None,
        description="A sub property of location. The original location of the object or the agent before the action.",
    )
    sportsEvent: Optional[
        Union[List[Union["SportsEvent", str]], "SportsEvent", str]
    ] = Field(
        default=None,
        description="A sub property of location. The sports event where this action occurred.",
    )
    distance: Optional[Union[List[Union["Distance", str]], "Distance", str]] = Field(
        default=None,
        description="The distance travelled, e.g. exercising or travelling.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.ExercisePlan import ExercisePlan
    from pydantic2_schemaorg.Place import Place
    from pydantic2_schemaorg.SportsActivityLocation import SportsActivityLocation
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.Diet import Diet
    from pydantic2_schemaorg.SportsTeam import SportsTeam
    from pydantic2_schemaorg.SportsEvent import SportsEvent
    from pydantic2_schemaorg.Distance import Distance
