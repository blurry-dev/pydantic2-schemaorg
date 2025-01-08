from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.AudioObject import AudioObject
from pydantic2_schemaorg.Book import Book


class Audiobook(AudioObject, Book):
    """An audiobook.

    See: https://schema.org/Audiobook
    Model depth: 4
    """

    type_: str = Field(default="Audiobook", alias="@type", const=True)
    duration: Optional[Union[List[Union["Duration", str]], "Duration", str]] = Field(
        default=None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    readBy: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="A person who reads (performs) the audiobook.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Duration import Duration
    from pydantic2_schemaorg.Person import Person
