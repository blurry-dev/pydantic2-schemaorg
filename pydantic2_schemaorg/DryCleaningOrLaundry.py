from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class DryCleaningOrLaundry(LocalBusiness):
    """A dry-cleaning business.

    See: https://schema.org/DryCleaningOrLaundry
    Model depth: 4
    """

    type_: str = Field(default="DryCleaningOrLaundry", alias="@type", const=True)
