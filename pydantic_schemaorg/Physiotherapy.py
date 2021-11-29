from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Physiotherapy(MedicalSpecialty, MedicalBusiness):
    """The practice of treatment of disease, injury, or deformity by physical methods such"
     "as massage, heat treatment, and exercise rather than by drugs or surgery..

    See https://schema.org/Physiotherapy.

    """

    locals().update({"@type": Field("Physiotherapy", const=True)})


Physiotherapy.update_forward_refs()