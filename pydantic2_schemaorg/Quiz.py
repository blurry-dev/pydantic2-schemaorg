from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LearningResource import LearningResource


class Quiz(LearningResource):
    """Quiz: A test of knowledge, skills and abilities.

    See: https://schema.org/Quiz
    Model depth: 4
    """

    type_: str = Field(default="Quiz", alias="@type", const=True)
