from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Comment import Comment


class CorrectionComment(Comment):
    """A [[comment]] that corrects [[CreativeWork]].

    See: https://schema.org/CorrectionComment
    Model depth: 4
    """

    type_: str = Field(default="CorrectionComment", alias="@type", const=True)
