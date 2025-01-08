from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.TechArticle import TechArticle


class APIReference(TechArticle):
    """Reference documentation for application programming interfaces (APIs).

    See: https://schema.org/APIReference
    Model depth: 5
    """

    type_: str = Field(default="APIReference", alias="@type", const=True)
    executableLibraryName: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = (
        Field(
            default=None,
            description="Library file name, e.g., mscorlib.dll, system.web.dll.",
        )
    )
    assembly: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Library file name, e.g., mscorlib.dll, system.web.dll.",
    )
    targetPlatform: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Type of app development: phone, Metro style, desktop, XBox, etc.",
    )
    programmingModel: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Indicates whether API is managed or unmanaged.",
    )
    assemblyVersion: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Associated product/technology version. E.g., .NET Framework 4.5.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
