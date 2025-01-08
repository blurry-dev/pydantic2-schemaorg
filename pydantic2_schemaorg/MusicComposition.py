from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class MusicComposition(CreativeWork):
    """A musical composition.

    See: https://schema.org/MusicComposition
    Model depth: 3
    """

    type_: str = Field(default="MusicComposition", alias="@type", const=True)
    composer: Optional[
        Union[List[Union["Person", "Organization", str]], "Person", "Organization", str]
    ] = Field(
        default=None,
        description="The person or organization who wrote a composition, or who is the composer of a work performed at some event.",
    )
    musicArrangement: Optional[
        Union[List[Union["MusicComposition", str]], "MusicComposition", str]
    ] = Field(
        default=None,
        description="An arrangement derived from the composition.",
    )
    musicCompositionForm: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = (
        Field(
            default=None,
            description="The type of composition (e.g. overture, sonata, symphony, etc.).",
        )
    )
    firstPerformance: Optional[Union[List[Union["Event", str]], "Event", str]] = Field(
        default=None,
        description="The date and place the work was first performed.",
    )
    musicalKey: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The key, mode, or scale this composition uses.",
    )
    recordedAs: Optional[
        Union[List[Union["MusicRecording", str]], "MusicRecording", str]
    ] = Field(
        default=None,
        description="An audio recording of the work.",
    )
    lyrics: Optional[Union[List[Union["CreativeWork", str]], "CreativeWork", str]] = (
        Field(
            default=None,
            description="The words in the song.",
        )
    )
    includedComposition: Optional[
        Union[List[Union["MusicComposition", str]], "MusicComposition", str]
    ] = Field(
        default=None,
        description="Smaller compositions included in this work (e.g. a movement in a symphony).",
    )
    iswcCode: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The International Standard Musical Work Code for the composition.",
    )
    lyricist: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="The person who wrote the words.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Event import Event
    from pydantic2_schemaorg.MusicRecording import MusicRecording
    from pydantic2_schemaorg.CreativeWork import CreativeWork
