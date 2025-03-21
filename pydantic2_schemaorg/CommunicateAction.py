from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.InteractAction import InteractAction


class CommunicateAction(InteractAction):
    """The act of conveying information to another person via a communication medium (instrument) such as speech,
     email, or telephone conversation.

    See: https://schema.org/CommunicateAction
    Model depth: 4
    """

    type_: str = Field(default="CommunicateAction", alias="@type", const=True)
    recipient: Optional[
        Union[
            List[Union["Organization", "Audience", "Person", "ContactPoint", str]],
            "Organization",
            "Audience",
            "Person",
            "ContactPoint",
            str,
        ]
    ] = Field(
        default=None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    inLanguage: Optional[
        Union[List[Union[str, "Text", "Language"]], str, "Text", "Language"]
    ] = Field(
        default=None,
        description="The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[availableLanguage]].",
    )
    about: Optional[Union[List[Union["Thing", str]], "Thing", str]] = Field(
        default=None,
        description="The subject matter of the content.",
    )
    language: Optional[Union[List[Union["Language", str]], "Language", str]] = Field(
        default=None,
        description="A sub property of instrument. The language used on this action.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.Audience import Audience
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.ContactPoint import ContactPoint
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Language import Language
    from pydantic2_schemaorg.Thing import Thing
