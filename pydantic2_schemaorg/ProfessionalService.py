from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class ProfessionalService(LocalBusiness):
    """Original definition: \"provider of professional services.\" The general [[ProfessionalService]] type
     for local businesses was deprecated due to confusion with [[Service]]. For reference, the types that it included
     were: [[Dentist]], [[AccountingService]], [[Attorney]], [[Notary]], as well as types for several kinds
     of [[HomeAndConstructionBusiness]]: [[Electrician]], [[GeneralContractor]], [[HousePainter]],
     [[Locksmith]], [[Plumber]], [[RoofingContractor]]. [[LegalService]] was introduced as a more inclusive
     supertype of [[Attorney]].

    See: https://schema.org/ProfessionalService
    Model depth: 4
    """

    type_: str = Field(default="ProfessionalService", alias="@type", const=True)
