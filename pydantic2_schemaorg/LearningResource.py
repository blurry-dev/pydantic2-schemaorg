from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class LearningResource(CreativeWork):
    """The LearningResource type can be used to indicate [[CreativeWork]]s (whether physical or digital) that
     have a particular and explicit orientation towards learning, education, skill acquisition, and other educational
     purposes. [[LearningResource]] is expected to be used as an addition to a primary type such as [[Book]], [[VideoObject]],
     [[Product]] etc. [[EducationEvent]] serves a similar purpose for event-like things (e.g. a [[Trip]]).
     A [[LearningResource]] may be created as a result of an [[EducationEvent]], for example by recording one.

    See: https://schema.org/LearningResource
    Model depth: 3
    """

    type_: str = Field(default="LearningResource", alias="@type", const=True)
    educationalUse: Optional[
        Union[List[Union[str, "Text", "DefinedTerm"]], str, "Text", "DefinedTerm"]
    ] = Field(
        default=None,
        description="The purpose of a work in the context of education; for example, 'assignment', 'group work'.",
    )
    learningResourceType: Optional[
        Union[List[Union[str, "Text", "DefinedTerm"]], str, "Text", "DefinedTerm"]
    ] = Field(
        default=None,
        description="The predominant type or kind characterizing the learning resource. For example, 'presentation', 'handout'.",
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
    educationalAlignment: Optional[
        Union[List[Union["AlignmentObject", str]], "AlignmentObject", str]
    ] = Field(
        default=None,
        description="An alignment to an established educational framework. This property should not be used where the nature of the alignment can be described using a simple property, for example to express that a resource [[teaches]] or [[assesses]] a competency.",
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
    assesses: Optional[
        Union[List[Union[str, "Text", "DefinedTerm"]], str, "Text", "DefinedTerm"]
    ] = Field(
        default=None,
        description="The item being described is intended to assess the competency or learning outcome defined by the referenced term.",
    )
    teaches: Optional[
        Union[List[Union[str, "Text", "DefinedTerm"]], str, "Text", "DefinedTerm"]
    ] = Field(
        default=None,
        description="The item being described is intended to help a person learn the competency or learning outcome defined by the referenced term.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.DefinedTerm import DefinedTerm
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.AlignmentObject import AlignmentObject
