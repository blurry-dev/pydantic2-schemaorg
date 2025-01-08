from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.RadioChannel import RadioChannel


class AMRadioChannel(RadioChannel):
    """A radio channel that uses AM.

    See: https://schema.org/AMRadioChannel
    Model depth: 5
    """

    type_: str = Field(default="AMRadioChannel", alias="@type", const=True)
