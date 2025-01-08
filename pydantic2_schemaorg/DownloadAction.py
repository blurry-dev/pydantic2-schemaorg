from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.TransferAction import TransferAction


class DownloadAction(TransferAction):
    """The act of downloading an object.

    See: https://schema.org/DownloadAction
    Model depth: 4
    """

    type_: str = Field(default="DownloadAction", alias="@type", const=True)
