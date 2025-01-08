from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.SocialMediaPosting import SocialMediaPosting


class BlogPosting(SocialMediaPosting):
    """A blog post.

    See: https://schema.org/BlogPosting
    Model depth: 5
    """

    type_: str = Field(default="BlogPosting", alias="@type", const=True)
