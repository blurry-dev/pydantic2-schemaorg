from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic.v1 import AnyUrl
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Event import Event


class CourseInstance(Event):
    """An instance of a [[Course]] which is distinct from other instances because it is offered at a different time
     or location or through different media or modes of study or to a specific section of students.

    See: https://schema.org/CourseInstance
    Model depth: 3
    """

    type_: str = Field(default="CourseInstance", alias="@type", const=True)
    courseMode: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description='The medium or means of delivery of the course instance or the mode of study, either as a text label (e.g. "online", "onsite" or "blended"; "synchronous" or "asynchronous"; "full-time" or "part-time") or as a URL reference to a term from a controlled vocabulary (e.g. https://ceds.ed.gov/element/001311#Asynchronous).',
    )
    instructor: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="A person assigned to instruct or provide instructional assistance for the [[CourseInstance]].",
    )
    courseWorkload: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description='The amount of work expected of students taking the course, often provided as a figure per week or per month, and may be broken down by type. For example, "2 hours of lectures, 1 hour of lab work and 3 hours of independent study per week".',
    )
    courseSchedule: Optional[Union[List[Union["Schedule", str]], "Schedule", str]] = (
        Field(
            default=None,
            description="Represents the length and pace of a course, expressed as a [[Schedule]].",
        )
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.Schedule import Schedule
