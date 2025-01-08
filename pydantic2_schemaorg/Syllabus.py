from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LearningResource import LearningResource


class Syllabus(LearningResource):
    """A syllabus that describes the material covered in a course, often with several such sections per [[Course]]
     so that a distinct [[timeRequired]] can be provided for that section of the [[Course]].

    See: https://schema.org/Syllabus
    Model depth: 4
    """

    type_: str = Field(default="Syllabus", alias="@type", const=True)
