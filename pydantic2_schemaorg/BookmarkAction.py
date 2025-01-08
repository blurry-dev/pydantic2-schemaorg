from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.OrganizeAction import OrganizeAction


class BookmarkAction(OrganizeAction):
    """An agent bookmarks/flags/labels/tags/marks an object.

    See: https://schema.org/BookmarkAction
    Model depth: 4
    """

    type_: str = Field(default="BookmarkAction", alias="@type", const=True)
