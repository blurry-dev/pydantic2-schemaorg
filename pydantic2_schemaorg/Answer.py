from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Comment import Comment


class Answer(Comment):
    """An answer offered to a question; perhaps correct, perhaps opinionated or wrong.

    See: https://schema.org/Answer
    Model depth: 4
    """

    type_: str = Field(default="Answer", alias="@type", const=True)
    parentItem: Optional[
        Union[
            List[Union["Comment", "CreativeWork", str]], "Comment", "CreativeWork", str
        ]
    ] = Field(
        default=None,
        description="The parent of a question, answer or item in general. Typically used for Q/A discussion threads e.g. a chain of comments with the first comment being an [[Article]] or other [[CreativeWork]]. See also [[comment]] which points from something to a comment about it.",
    )
    answerExplanation: Optional[
        Union[List[Union["Comment", "WebContent", str]], "Comment", "WebContent", str]
    ] = Field(
        default=None,
        description="A step-by-step or full explanation about Answer. Can outline how this Answer was achieved or contain more broad clarification or statement about it.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Comment import Comment
    from pydantic2_schemaorg.CreativeWork import CreativeWork
    from pydantic2_schemaorg.WebContent import WebContent
