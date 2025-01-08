from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEntity import MedicalEntity


class MedicalTest(MedicalEntity):
    """Any medical test, typically performed for diagnostic purposes.

    See: https://schema.org/MedicalTest
    Model depth: 3
    """

    type_: str = Field(default="MedicalTest", alias="@type", const=True)
    signDetected: Optional[
        Union[List[Union["MedicalSign", str]], "MedicalSign", str]
    ] = Field(
        default=None,
        description="A sign detected by the test.",
    )
    affectedBy: Optional[Union[List[Union["Drug", str]], "Drug", str]] = Field(
        default=None,
        description="Drugs that affect the test's results.",
    )
    usedToDiagnose: Optional[
        Union[List[Union["MedicalCondition", str]], "MedicalCondition", str]
    ] = Field(
        default=None,
        description="A condition the test is used to diagnose.",
    )
    normalRange: Optional[
        Union[
            List[Union[str, "Text", "MedicalEnumeration"]],
            str,
            "Text",
            "MedicalEnumeration",
        ]
    ] = Field(
        default=None,
        description="Range of acceptable values for a typical patient, when applicable.",
    )
    usesDevice: Optional[
        Union[List[Union["MedicalDevice", str]], "MedicalDevice", str]
    ] = Field(
        default=None,
        description="Device used to perform the test.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.MedicalSign import MedicalSign
    from pydantic2_schemaorg.Drug import Drug
    from pydantic2_schemaorg.MedicalCondition import MedicalCondition
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.MedicalEnumeration import MedicalEnumeration
    from pydantic2_schemaorg.MedicalDevice import MedicalDevice
