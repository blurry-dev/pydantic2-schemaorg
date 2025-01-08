from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class Grant(Intangible):
    """A grant, typically financial or otherwise quantifiable, of resources. Typically a [[funder]] sponsors
     some [[MonetaryAmount]] to an [[Organization]] or [[Person]], sometimes not necessarily via a dedicated
     or long-lived [[Project]], resulting in one or more outputs, or [[fundedItem]]s. For financial sponsorship,
     indicate the [[funder]] of a [[MonetaryGrant]]. For non-financial support, indicate [[sponsor]] of [[Grant]]s
     of resources (e.g. office space). Grants support activities directed towards some agreed collective goals,
     often but not always organized as [[Project]]s. Long-lived projects are sometimes sponsored by a variety
     of grants over time, but it is also common for a project to be associated with a single grant. The amount of a [[Grant]]
     is represented using [[amount]] as a [[MonetaryAmount]].

    See: https://schema.org/Grant
    Model depth: 3
    """

    type_: str = Field(default="Grant", alias="@type", const=True)
    funder: Optional[
        Union[List[Union["Person", "Organization", str]], "Person", "Organization", str]
    ] = Field(
        default=None,
        description="A person or organization that supports (sponsors) something through some kind of financial contribution.",
    )
    fundedItem: Optional[
        Union[
            List[
                Union[
                    "Event",
                    "CreativeWork",
                    "BioChemEntity",
                    "Person",
                    "MedicalEntity",
                    "Product",
                    "Organization",
                    str,
                ]
            ],
            "Event",
            "CreativeWork",
            "BioChemEntity",
            "Person",
            "MedicalEntity",
            "Product",
            "Organization",
            str,
        ]
    ] = Field(
        default=None,
        description="Indicates something directly or indirectly funded or sponsored through a [[Grant]]. See also [[ownershipFundingInfo]].",
    )
    sponsor: Optional[
        Union[List[Union["Person", "Organization", str]], "Person", "Organization", str]
    ] = Field(
        default=None,
        description="A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.Event import Event
    from pydantic2_schemaorg.CreativeWork import CreativeWork
    from pydantic2_schemaorg.BioChemEntity import BioChemEntity
    from pydantic2_schemaorg.MedicalEntity import MedicalEntity
    from pydantic2_schemaorg.Product import Product
