from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class SoftwareSourceCode(CreativeWork):
    """Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts,
     templates.

    See: https://schema.org/SoftwareSourceCode
    Model depth: 3
    """

    type_: str = Field(default="SoftwareSourceCode", alias="@type", const=True)
    targetProduct: Optional[
        Union[List[Union["SoftwareApplication", str]], "SoftwareApplication", str]
    ] = Field(
        default=None,
        description="Target Operating System / Product to which the code applies. If applies to several versions, just the product name can be used.",
    )
    codeRepository: Optional[
        Union[List[Union[AnyUrl, "URL", str]], AnyUrl, "URL", str]
    ] = Field(
        default=None,
        description="Link to the repository where the un-compiled, human readable code and related code is located (SVN, GitHub, CodePlex).",
    )
    runtimePlatform: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Runtime platform or script interpreter dependencies (example: Java v1, Python 2.3, .NET Framework 3.0).",
    )
    sampleType: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="What type of code sample: full (compile ready) solution, code snippet, inline code, scripts, template.",
    )
    programmingLanguage: Optional[
        Union[
            List[Union[str, "Text", "ComputerLanguage"]],
            str,
            "Text",
            "ComputerLanguage",
        ]
    ] = Field(
        default=None,
        description="The computer programming language.",
    )
    runtime: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Runtime platform or script interpreter dependencies (example: Java v1, Python 2.3, .NET Framework 3.0).",
    )
    codeSampleType: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="What type of code sample: full (compile ready) solution, code snippet, inline code, scripts, template.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.SoftwareApplication import SoftwareApplication
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.ComputerLanguage import ComputerLanguage
