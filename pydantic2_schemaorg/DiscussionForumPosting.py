from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.SocialMediaPosting import SocialMediaPosting


class DiscussionForumPosting(SocialMediaPosting):
    """A posting to a discussion forum.

    See: https://schema.org/DiscussionForumPosting
    Model depth: 5
    """

    type_: str = Field(default="DiscussionForumPosting", alias="@type", const=True)
