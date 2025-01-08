from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class EducationalOccupationalCredential(CreativeWork):
    """An educational or occupational credential. A diploma, academic degree, certification, qualification,
     badge, etc., that may be awarded to a person or other entity that meets the requirements defined by the credentialer.

    See: https://schema.org/EducationalOccupationalCredential
    Model depth: 3
    """

    type_: str = Field(
        default="EducationalOccupationalCredential", alias="@type", const=True
    )
    validIn: Optional[
        Union[List[Union["AdministrativeArea", str]], "AdministrativeArea", str]
    ] = Field(
        default=None,
        description="The geographic area where the item is valid. Applies for example to a [[Permit]], a [[Certification]], or an [[EducationalOccupationalCredential]].",
    )
    recognizedBy: Optional[
        Union[List[Union["Organization", str]], "Organization", str]
    ] = Field(
        default=None,
        description="An organization that acknowledges the validity, value or utility of a credential. Note: recognition may include a process of quality assurance or accreditation.",
    )
    educationalLevel: Optional[
        Union[
            List[Union[AnyUrl, "URL", str, "Text", "DefinedTerm"]],
            AnyUrl,
            "URL",
            str,
            "Text",
            "DefinedTerm",
        ]
    ] = Field(
        default=None,
        description="The level in terms of progression through an educational or training context. Examples of educational levels include 'beginner', 'intermediate' or 'advanced', and formal sets of level indicators.",
    )
    competencyRequired: Optional[
        Union[
            List[Union[AnyUrl, "URL", str, "Text", "DefinedTerm"]],
            AnyUrl,
            "URL",
            str,
            "Text",
            "DefinedTerm",
        ]
    ] = Field(
        default=None,
        description="Knowledge, skill, ability or personal attribute that must be demonstrated by a person or other entity in order to do something such as earn an Educational Occupational Credential or understand a LearningResource.",
    )
    validFor: Optional[Union[List[Union["Duration", str]], "Duration", str]] = Field(
        default=None,
        description="The duration of validity of a permit or similar thing.",
    )
    credentialCategory: Optional[
        Union[
            List[Union[AnyUrl, "URL", str, "Text", "DefinedTerm"]],
            AnyUrl,
            "URL",
            str,
            "Text",
            "DefinedTerm",
        ]
    ] = Field(
        default=None,
        description='The category or type of credential being described, for example "degree”, “certificate”, “badge”, or more specific term.',
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.DefinedTerm import DefinedTerm
    from pydantic2_schemaorg.Duration import Duration
