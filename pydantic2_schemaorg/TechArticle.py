from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Article import Article


class TechArticle(Article):
    """A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications,
     etc.

    See: https://schema.org/TechArticle
    Model depth: 4
    """

    type_: str = Field(default="TechArticle", alias="@type", const=True)
    dependencies: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Prerequisites needed to fulfill steps in article.",
    )
    proficiencyLevel: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Proficiency needed for this content; expected values: 'Beginner', 'Expert'.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
