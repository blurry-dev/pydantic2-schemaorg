from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl


from pydantic.v1 import Field
from pydantic2_schemaorg.LifestyleModification import LifestyleModification


class PhysicalActivity(LifestyleModification):
    """Any bodily activity that enhances or maintains physical fitness and overall health and wellness. Includes
     activity that is part of daily living and routine, structured exercise, and exercise prescribed as part of
     a medical treatment or recovery plan.

    See: https://schema.org/PhysicalActivity
    Model depth: 4
    """

    type_: str = Field(default="PhysicalActivity", alias="@type", const=True)
    pathophysiology: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Changes in the normal mechanical, physical, and biochemical functions that are associated with this activity or condition.",
    )
    epidemiology: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The characteristics of associated patients, such as age, gender, race etc.",
    )
    category: Optional[
        Union[
            List[
                Union[
                    AnyUrl,
                    "URL",
                    str,
                    "Text",
                    "PhysicalActivityCategory",
                    "CategoryCode",
                    "Thing",
                ]
            ],
            AnyUrl,
            "URL",
            str,
            "Text",
            "PhysicalActivityCategory",
            "CategoryCode",
            "Thing",
        ]
    ] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.",
    )
    associatedAnatomy: Optional[
        Union[
            List[
                Union[
                    "SuperficialAnatomy", "AnatomicalSystem", "AnatomicalStructure", str
                ]
            ],
            "SuperficialAnatomy",
            "AnatomicalSystem",
            "AnatomicalStructure",
            str,
        ]
    ] = Field(
        default=None,
        description="The anatomy of the underlying organ system or structures associated with this entity.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
    from pydantic2_schemaorg.CategoryCode import CategoryCode
    from pydantic2_schemaorg.Thing import Thing
    from pydantic2_schemaorg.SuperficialAnatomy import SuperficialAnatomy
    from pydantic2_schemaorg.AnatomicalSystem import AnatomicalSystem
    from pydantic2_schemaorg.AnatomicalStructure import AnatomicalStructure
