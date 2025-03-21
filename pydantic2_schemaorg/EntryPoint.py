from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class EntryPoint(Intangible):
    """An entry point, within some Web-based protocol.

    See: https://schema.org/EntryPoint
    Model depth: 3
    """

    type_: str = Field(default="EntryPoint", alias="@type", const=True)
    contentType: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The supported content type(s) for an EntryPoint response.",
    )
    actionPlatform: Optional[
        Union[
            List[Union[AnyUrl, "URL", str, "Text", "DigitalPlatformEnumeration"]],
            AnyUrl,
            "URL",
            str,
            "Text",
            "DigitalPlatformEnumeration",
        ]
    ] = Field(
        default=None,
        description="The high level platform(s) where the Action can be performed for the given URL. To specify a specific application or operating system instance, use actionApplication.",
    )
    application: Optional[
        Union[List[Union["SoftwareApplication", str]], "SoftwareApplication", str]
    ] = Field(
        default=None,
        description="An application that can complete the request.",
    )
    httpMethod: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="An HTTP method that specifies the appropriate HTTP method for a request to an HTTP EntryPoint. Values are capitalized strings as used in HTTP.",
    )
    encodingType: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The supported encoding type(s) for an EntryPoint request.",
    )
    urlTemplate: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="An url template (RFC6570) that will be used to construct the target of the execution of the action.",
    )
    actionApplication: Optional[
        Union[List[Union["SoftwareApplication", str]], "SoftwareApplication", str]
    ] = Field(
        default=None,
        description="An application that can complete the request.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.DigitalPlatformEnumeration import (
        DigitalPlatformEnumeration,
    )
    from pydantic2_schemaorg.SoftwareApplication import SoftwareApplication
