from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Comment import Comment


class Question(Comment):
    """A specific question - e.g. from a user seeking answers online, or collected in a Frequently Asked Questions
     (FAQ) document.

    See: https://schema.org/Question
    Model depth: 4
    """

    type_: str = Field(default="Question", alias="@type", const=True)
    parentItem: Optional[
        Union[
            List[Union["Comment", "CreativeWork", str]], "Comment", "CreativeWork", str
        ]
    ] = Field(
        default=None,
        description="The parent of a question, answer or item in general. Typically used for Q/A discussion threads e.g. a chain of comments with the first comment being an [[Article]] or other [[CreativeWork]]. See also [[comment]] which points from something to a comment about it.",
    )
    suggestedAnswer: Optional[
        Union[List[Union["Answer", "ItemList", str]], "Answer", "ItemList", str]
    ] = Field(
        default=None,
        description="An answer (possibly one of several, possibly incorrect) to a Question, e.g. on a Question/Answer site.",
    )
    eduQuestionType: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description='For questions that are part of learning resources (e.g. Quiz), eduQuestionType indicates the format of question being given. Example: "Multiple choice", "Open ended", "Flashcard".',
    )
    answerCount: Optional[
        Union[List[Union[int, "Integer", str]], int, "Integer", str]
    ] = Field(
        default=None,
        description="The number of answers this question has received.",
    )
    acceptedAnswer: Optional[
        Union[List[Union["Answer", "ItemList", str]], "Answer", "ItemList", str]
    ] = Field(
        default=None,
        description="The answer(s) that has been accepted as best, typically on a Question/Answer site. Sites vary in their selection mechanisms, e.g. drawing on community opinion and/or the view of the Question author.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Comment import Comment
    from pydantic2_schemaorg.CreativeWork import CreativeWork
    from pydantic2_schemaorg.Answer import Answer
    from pydantic2_schemaorg.ItemList import ItemList
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Integer import Integer
