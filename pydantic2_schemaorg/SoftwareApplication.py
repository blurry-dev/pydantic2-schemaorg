from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class SoftwareApplication(CreativeWork):
    """A software application.

    See: https://schema.org/SoftwareApplication
    Model depth: 3
    """

    type_: str = Field(default="SoftwareApplication", alias="@type", const=True)
    softwareAddOn: Optional[
        Union[List[Union["SoftwareApplication", str]], "SoftwareApplication", str]
    ] = Field(
        default=None,
        description="Additional content for a software application.",
    )
    downloadUrl: Optional[
        Union[List[Union[AnyUrl, "URL", str]], AnyUrl, "URL", str]
    ] = Field(
        default=None,
        description="If the file can be downloaded, URL to download the binary.",
    )
    storageRequirements: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description="Storage requirements (free space required).",
    )
    applicationSuite: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The name of the application suite to which the application belongs (e.g. Excel belongs to Office).",
    )
    softwareRequirements: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description="Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (examples: DirectX, Java or .NET runtime).",
    )
    applicationCategory: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description="Type of software application, e.g. 'Game, Multimedia'.",
    )
    countriesNotSupported: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = (
        Field(
            default=None,
            description="Countries for which the application is not supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.",
        )
    )
    supportingData: Optional[Union[List[Union["DataFeed", str]], "DataFeed", str]] = (
        Field(
            default=None,
            description="Supporting data for a SoftwareApplication.",
        )
    )
    softwareHelp: Optional[
        Union[List[Union["CreativeWork", str]], "CreativeWork", str]
    ] = Field(
        default=None,
        description="Software application help.",
    )
    releaseNotes: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description="Description of what changed in this version.",
    )
    processorRequirements: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = (
        Field(
            default=None,
            description="Processor architecture required to run the application (e.g. IA64).",
        )
    )
    featureList: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description="Features or modules provided by this application (and possibly required by other applications).",
    )
    applicationSubCategory: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description="Subcategory of the application, e.g. 'Arcade Game'.",
    )
    fileSize: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Size of the application / package (e.g. 18MB). In the absence of a unit (MB, KB etc.), KB will be assumed.",
    )
    softwareVersion: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Version of the software instance.",
    )
    device: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Device required to run the application. Used in cases where a specific make/model is required to run the application.",
    )
    screenshot: Optional[
        Union[
            List[Union[AnyUrl, "URL", "ImageObject", str]],
            AnyUrl,
            "URL",
            "ImageObject",
            str,
        ]
    ] = Field(
        default=None,
        description="A link to a screenshot image of the app.",
    )
    permissions: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Permission(s) required to run the app (for example, a mobile app may require full internet access or may run only on wifi).",
    )
    requirements: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description="Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (examples: DirectX, Java or .NET runtime).",
    )
    installUrl: Optional[Union[List[Union[AnyUrl, "URL", str]], AnyUrl, "URL", str]] = (
        Field(
            default=None,
            description="URL at which the app may be installed, if different from the URL of the item.",
        )
    )
    memoryRequirements: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description="Minimum memory requirements.",
    )
    countriesSupported: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Countries for which the application is supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.",
    )
    operatingSystem: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Operating systems supported (Windows 7, OS X 10.6, Android 1.6).",
    )
    availableOnDevice: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Device required to run the application. Used in cases where a specific make/model is required to run the application.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.DataFeed import DataFeed
    from pydantic2_schemaorg.CreativeWork import CreativeWork
    from pydantic2_schemaorg.ImageObject import ImageObject
