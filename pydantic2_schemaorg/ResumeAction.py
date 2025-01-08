from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ControlAction import ControlAction


class ResumeAction(ControlAction):
    """The act of resuming a device or application which was formerly paused (e.g. resume music playback or resume
     a timer).

    See: https://schema.org/ResumeAction
    Model depth: 4
    """

    type_: str = Field(default="ResumeAction", alias="@type", const=True)
