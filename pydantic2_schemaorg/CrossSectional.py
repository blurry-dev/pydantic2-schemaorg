from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalObservationalStudyDesign import (
    MedicalObservationalStudyDesign,
)


class CrossSectional(MedicalObservationalStudyDesign):
    """Studies carried out on pre-existing data (usually from 'snapshot' surveys), such as that collected by the
     Census Bureau. Sometimes called Prevalence Studies.

    See: https://schema.org/CrossSectional
    Model depth: 6
    """

    type_: str = Field(default="CrossSectional", alias="@type", const=True)
