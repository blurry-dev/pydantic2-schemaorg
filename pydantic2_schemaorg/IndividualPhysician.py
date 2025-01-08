from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Physician import Physician


class IndividualPhysician(Physician):
    """An individual medical practitioner. For their official address use [[address]], for affiliations to hospitals
     use [[hospitalAffiliation]]. The [[practicesAt]] property can be used to indicate [[MedicalOrganization]]
     hospitals, clinics, pharmacies etc. where this physician practices.

    See: https://schema.org/IndividualPhysician
    Model depth: 5
    """

    type_: str = Field(default="IndividualPhysician", alias="@type", const=True)
    practicesAt: Optional[
        Union[List[Union["MedicalOrganization", str]], "MedicalOrganization", str]
    ] = Field(
        default=None,
        description="A [[MedicalOrganization]] where the [[IndividualPhysician]] practices.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.MedicalOrganization import MedicalOrganization
