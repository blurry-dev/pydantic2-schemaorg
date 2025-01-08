from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic2_schemaorg.MedicalOrganization import MedicalOrganization


class Physician(MedicalBusiness, MedicalOrganization):
    """An individual physician or a physician's office considered as a [[MedicalOrganization]].

    See: https://schema.org/Physician
    Model depth: 4
    """

    type_: str = Field(default="Physician", alias="@type", const=True)
    occupationalCategory: Optional[
        Union[List[Union[str, "Text", "CategoryCode"]], str, "Text", "CategoryCode"]
    ] = Field(
        default=None,
        description="A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html), [ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided. Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.",
    )
    hospitalAffiliation: Optional[
        Union[List[Union["Hospital", str]], "Hospital", str]
    ] = Field(
        default=None,
        description="A hospital with which the physician or office is affiliated.",
    )
    availableService: Optional[
        Union[
            List[Union["MedicalTherapy", "MedicalProcedure", "MedicalTest", str]],
            "MedicalTherapy",
            "MedicalProcedure",
            "MedicalTest",
            str,
        ]
    ] = Field(
        default=None,
        description="A medical service available from this provider.",
    )
    usNPI: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description='A <a href="https://en.wikipedia.org/wiki/National_Provider_Identifier">National Provider Identifier</a> (NPI) is a unique 10-digit identification number issued to health care providers in the United States by the Centers for Medicare and Medicaid Services.',
    )
    medicalSpecialty: Optional[
        Union[List[Union["MedicalSpecialty", str]], "MedicalSpecialty", str]
    ] = Field(
        default=None,
        description="A medical specialty of the provider.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.CategoryCode import CategoryCode
    from pydantic2_schemaorg.Hospital import Hospital
    from pydantic2_schemaorg.MedicalTherapy import MedicalTherapy
    from pydantic2_schemaorg.MedicalProcedure import MedicalProcedure
    from pydantic2_schemaorg.MedicalTest import MedicalTest
    from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty
