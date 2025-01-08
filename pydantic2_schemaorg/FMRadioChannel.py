from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.RadioChannel import RadioChannel


class FMRadioChannel(RadioChannel):
    """A radio channel that uses FM.

    See: https://schema.org/FMRadioChannel
    Model depth: 5
    """

    type_: str = Field(default="FMRadioChannel", alias="@type", const=True)
